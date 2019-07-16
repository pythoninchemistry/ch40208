HANDOUTS = ['week_3/handout_3.pdf']

rule all:
	input:
		HANDOUTS

rule handout_3:
	input:
		'week_3/handout_source/handout_3.tex',
	output:
		'week_3/handout_3.pdf'
	shell:
		"""
		cd week_3/handout_source && pdflatex handout_3.tex && bibtex handout_3.aux && pdflatex handout_3.tex && pdflatex handout_3.tex && cp handout_3.pdf ../
		"""
