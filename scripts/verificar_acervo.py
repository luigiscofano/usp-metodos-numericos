"""Valida esquema e sanitização básica sem executar o acervo histórico."""
from pathlib import Path
import json
import re
import nbformat

ROOT=Path(__file__).resolve().parents[1]


def main():
    files=sorted((ROOT/'acervo').glob('*.ipynb'))
    for path in files:
        notebook=nbformat.read(path,as_version=4)
        nbformat.validate(notebook)
        for cell in notebook.cells:
            if cell.cell_type=='code':
                assert cell.execution_count is None and not cell.outputs, path
            assert 'data:image/' not in cell.source, path
            assert not re.search(r'https?://(?:drive\.google\.com|colab\.research\.google\.com|classroom\.google\.com)',cell.source),path
        print('PASS acervo sanitizado',path.name)
    inventory=json.loads((ROOT/'docs/inventario.json').read_text())
    assert {p.name for p in files}=={item['arquivo'] for item in inventory}
    for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
        nbformat.validate(nbformat.read(path,as_version=4))
    return 0


if __name__=='__main__':raise SystemExit(main())
