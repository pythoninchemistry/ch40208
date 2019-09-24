HANDOUTS = ['week_1/handout_1.pdf']

rule all:
	input:
		HANDOUTS

rule handout_1:
	input:
		'week_1/handout_source/handout_1.tex',
		'week_1/handout_source/handout_1.bib',
		'week_1/handout_source/chem_data_py.pdf'
	output:
		'week_1/handout_1.pdf'
	shell:
		"""
		cd week_1/handout_source && pdflatex handout_1.tex && bibtex handout_1.aux && pdflatex handout_1.tex && pdflatex handout_1.tex && cp handout_1.pdf ../
		"""

rule handout_1_plots:
	input:
		'week_1/handout_source/plots.py'
	output:
		'week_1/handout_source/chem_data_py.pdf'
	shell:
		"""
		cd week_1/handout_source && python plots.py && cd ../
		"""