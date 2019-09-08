HANDOUTS = ['week_2/handout_2.pdf']

rule all:
	input:
		HANDOUTS

rule handout_2:
	input:
		'week_2/handout_source/handout_2.tex',
		'week_2/handout_source/x_squared.pdf',
	output:
		'week_2/handout_2.pdf'
	shell:
		"""
		cd week_2/handout_source && pdflatex handout_2.tex && bibtex handout_2.aux && pdflatex handout_2.tex && pdflatex handout_2.tex && cp handout_2.pdf ../
		"""

rule plots:
	input:
		'week_2/handout_source/plots.py',
	output:
		'week_2/handout_source/x_squared.pdf'
	shell:
		"""
		cd week_2/handout_source && python plots.py && cd ../../
		"""
