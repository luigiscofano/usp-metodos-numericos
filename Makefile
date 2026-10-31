PYTHON = python3
.PHONY: install test notebooks local html clean
install:
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m ipykernel install --user --name python3 --display-name 'Python 3'
test:
	$(PYTHON) -m pytest -q
notebooks:
	MPLBACKEND=Agg $(PYTHON) scripts/executar_notebooks.py
local:
	MPLBACKEND=Agg $(PYTHON) scripts/executar_sem_kernel.py
html: notebooks
clean:
	rm -rf build .pytest_cache
