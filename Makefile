target ?= main
all: clean imported_libs
	pyinstaller -F ${target}.py --onefile
	-rm -rf ${target}
	mkdir ${target}
	cp -R dist/${target} app ${target}
	tar czf ${target}.tgz ${target}
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
	-rm -rf ${target}.spec
	-rm -rf ${target}.tgz

