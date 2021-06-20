unslashedDir=$(patsubst %/,%,$(dir $(1)))
pathOfThisMakefile:=$(call unslashedDir,$(lastword $(MAKEFILE_LIST)))
buildDirectory:=build
pathOfTexFile=envelope_label.tex

default: | ${buildDirectory}
	miktex-xetex --quiet --undump=xelatex --interaction=nonstopmode --output-directory="${buildDirectory}" --aux-directory="${buildDirectory}" "${pathOfTexFile}"
	

${buildDirectory}:
	@echo "====== CREATING THE BUILD FOLDER ======="
	@echo "buildDirectory: ${buildDirectory}"
	mkdir --parents "${buildDirectory}"
	@echo -ne "\n"
