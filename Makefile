all: clean imported_libs
	pyinstaller -F main.py --onefile
	@echo 'done'

imported_libs:
	-@rm imported_libs.py
	-@./imported_libs.sh
	@echo ---------------------start imported.py---------------------
	@cat imported_libs.py
	@echo ---------------------end imported.py---------------------

clean:
	-rm -rf dist
	-rm -rf build
	find . -name __pycache__ | xargs rm -rf
	-rm -rf main.spec

