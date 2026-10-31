"""Executa apenas a edição de estudo em kernel novo e exporta HTML para build/."""
from pathlib import Path
import argparse
import json
import os
import time
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--atualizar',action='store_true',help='Versiona contadores e saídas textuais; imagens ficam em assets/figuras.')
    args=parser.parse_args()
    out=ROOT/'build';out.mkdir(exist_ok=True)
    os.environ.setdefault('MPLBACKEND','Agg')
    results=[]
    for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
        notebook=nbformat.read(path,as_version=4)
        start=time.perf_counter()
        try:
            NotebookClient(notebook,timeout=180,kernel_name='python3',resources={'metadata':{'path':str(ROOT)}}).execute()
            nbformat.write(notebook,out/path.name)
            html,_=HTMLExporter().from_notebook_node(notebook)
            (out/(path.stem+'.html')).write_text(html)
            figures=sorted((ROOT/'assets/figuras').glob(path.stem[:2]+'_*.svg'))
            if args.atualizar:
                # Mantém texto, resultados e contadores sem duplicar PNGs no JSON.
                for cell in notebook.cells:
                    if cell.cell_type=='code':
                        cell.outputs=[o for o in cell.outputs if o.output_type not in {'display_data','execute_result'} or 'image/png' not in o.get('data',{})]
                        cell.metadata={}
                notebook.cells=[c for c in notebook.cells if c.get('metadata',{}).get('galeria') is not True]
                gallery=nbformat.v4.new_markdown_cell('## Figuras desta execução\n\n'+ '\n\n'.join(f'![{p.stem}](../assets/figuras/{p.name})' for p in figures))
                gallery.metadata['galeria']=True
                notebook.cells.append(gallery)
                nbformat.write(notebook,path)
            item={'notebook':path.name,'passou':True,'celulas_codigo':sum(c.cell_type=='code' for c in notebook.cells),'segundos':round(time.perf_counter()-start,3),'figuras':[p.name for p in figures]}
        except Exception as error:
            item={'notebook':path.name,'passou':False,'erro':str(error)[-4000:]}
        results.append(item)
        print(('PASS ' if item['passou'] else 'FAIL ')+path.name,flush=True)
        (out/'resultados-notebooks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    return 0 if results and all(x['passou'] for x in results) else 1


if __name__=='__main__':
    raise SystemExit(main())
