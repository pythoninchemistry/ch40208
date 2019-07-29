HANDOUTS = ['week_4/handout_4.pdf']

rule all:
	input:
		HANDOUTS

rule handout_4:
	input:
		'week_4/handout_source/handout_4.tex',
	output:
		'week_4/handout_4.pdf'
	shell:
		"""
		cd week_4/handout_source && pdflatex handout_4.tex && pdflatex handout_4.tex && cp handout_4.pdf ../
		"""
