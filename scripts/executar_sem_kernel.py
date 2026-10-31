"""Executa células via IPython em processo novo; alternativa local sem servidor Jupyter.

Não substitui o teste de kernel Jupyter feito por executar_notebooks.py no CI.
"""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys
import time
import nbformat
from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.capture import capture_output
from nbconvert import HTMLExporter

ROOT=Path(__file__).resolve().parents[1]


def execute(path, update):
    notebook=nbformat.read(path,as_version=4)
    notebook.cells=[c for c in notebook.cells if not c.get('metadata',{}).get('galeria')]
    shell=InteractiveShell.instance()
    os.chdir(ROOT)
    count=0
    for cell in notebook.cells:
        if cell.cell_type!='code':continue
        count+=1
        with capture_output() as captured:
            result=shell.run_cell(cell.source,store_history=True)
        if result.error_before_exec or result.error_in_exec:
            raise RuntimeError(captured.stdout+'\n'+captured.stderr)
        cell.execution_count=count
        cell.outputs=[]
        for name,text in [('stdout',captured.stdout),('stderr',captured.stderr)]:
            if text:cell.outputs.append(nbformat.v4.new_output('stream',name=name,text=text))
    figures=sorted((ROOT/'assets/figuras').glob(path.stem[:2]+'_*.svg'))
    gallery=nbformat.v4.new_markdown_cell('## Figuras desta execução\n\n'+'\n\n'.join(f'![{p.stem}](../assets/figuras/{p.name})' for p in figures))
    gallery.metadata['galeria']=True;notebook.cells.append(gallery)
    notebook.metadata['validacao_local']={'modo':'IPython em processo isolado, sem servidor/kernel Jupyter','data':'2026-10-31'}
    output=ROOT/'build';output.mkdir(exist_ok=True)
    nbformat.write(notebook,output/path.name)
    html,_=HTMLExporter().from_notebook_node(notebook)
    (output/(path.stem+'.html')).write_text(html)
    if update:nbformat.write(notebook,path)
    print(json.dumps({'notebook':path.name,'passou':True,'celulas_codigo':count,'figuras':[p.name for p in figures]},ensure_ascii=False))


def main():
    p=argparse.ArgumentParser();p.add_argument('--arquivo',type=Path);p.add_argument('--atualizar',action='store_true');args=p.parse_args()
    os.environ.setdefault('MPLBACKEND','Agg')
    if args.arquivo:
        execute(args.arquivo.resolve(),args.atualizar);return 0
    records=[]
    for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
        start=time.perf_counter()
        command=[sys.executable,str(Path(__file__).resolve()),'--arquivo',str(path)]
        if args.atualizar:command+=['--atualizar']
        r=subprocess.run(command,capture_output=True,text=True,timeout=240)
        if r.returncode:
            item={'notebook':path.name,'passou':False,'erro':r.stdout[-3000:]+r.stderr[-3000:]}
        else:item=json.loads(r.stdout.strip().splitlines()[-1])
        item['segundos']=round(time.perf_counter()-start,3);records.append(item)
        print(('PASS ' if item['passou'] else 'FAIL ')+path.name,flush=True)
    (ROOT/'build/resultados-sem-kernel.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    return 0 if all(x['passou'] for x in records) else 1


if __name__=='__main__':raise SystemExit(main())
