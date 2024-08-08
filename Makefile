VENV_ACTIVATE = . env/bin/activate &&

install:
	python -m venv env && $(VENV_ACTIVATE) pip install -r requirements.txt

run:
	$(VENV_ACTIVATE) python main.py
	
uninstall:
	rm -rf env

.PHONY: install run uninstall
