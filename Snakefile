HANDOUTS = ['week_1/handout_1.pdf']

rule all:
	input:
		HANDOUTS

rule handout_1:
	input:
		'week_1/handout_source/handout_1.tex'
	output:
		'week_1/handout_1.pdf'
	shell:
		"""
		cd week_1/handout_source && pdflatex handout_1.tex && bibtex handout_1.aux && cp handout_1.pdf ../
		"""