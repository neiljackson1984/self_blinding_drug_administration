unslashedDir=$(patsubst %/,%,$(dir $(1)))
pathOfThisMakefile:=$(call unslashedDir,$(lastword $(MAKEFILE_LIST)))
pathOfDeployScript:=${pathOfThisMakefile}/self_blinding.py
venv:=$(shell cd "$(abspath $(dir ${pathOfDeployScript}))" > /dev/null 2>&1; pipenv --venv || echo initializeVenv)



.PHONY: initializeVenv

default: |  ${venv}
	@echo "====== running $(pathOfDeployScript) ======="
	# @echo "venv is ${venv} ======="
	cd "$(abspath $(dir ${pathOfDeployScript}))"; \
	pipenv run python "$(notdir ${pathOfDeployScript})" \

${venv}: $(dir ${pathOfDeployScript})Pipfile $(dir ${pathOfDeployScript})Pipfile.lock
	@echo "====== INITIALIZING VIRTUAL ENVIRONMENT ======= "
	@echo "target: $@"
	cd "$(abspath $(dir ${pathOfDeployScript}))"; pipenv install
	touch $(shell cd "$(abspath $(dir ${pathOfDeployScript}))" > /dev/null 2>&1; pipenv --venv)
	@echo -ne "\n"

.SILENT:
