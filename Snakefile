HANDOUTS = ['week_5/handout_5.pdf']

rule all:
	input:
		HANDOUTS,

rule handout_4:
	input:
		'week_5/handout_source/handout_5.tex',
	output:
		'week_5/handout_5.pdf'
	shell:
		"""
		cd week_5/handout_source && pdflatex handout_5.tex && pdflatex handout_5.tex && cp handout_5.pdf ../
		"""
