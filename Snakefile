HANDOUTS = ['week_1/handout_1.pdf', 'week_2/handout_2.pdf', 'week_3/handout_3.pdf']

rule all:
	input:
		HANDOUTS,
    'week_3/mini.mp4'

rule handout_3:
	input:
		'week_3/handout_source/handout_3.tex',
	output:
		'week_3/handout_3.pdf'
	shell:
		"""
		cd week_3/handout_source && pdflatex handout_3.tex && pdflatex handout_3.tex && cp handout_3.pdf ../
		"""

rule mini:
	input:
		'week_3/plots.py',
	output:
		'week_3/mini.mp4'
	shell:
		"""
		python week_3/plots.py
		ffmpeg -y -framerate 2 -i week_3/mini/%01d.png -pix_fmt yuv420p week_3/mini.mp4
    """

rule handout_2:
	input:
		'week_2/handout_source/handout_2.tex',
		'week_2/handout_source/x_squared.pdf',
		'week_2/handout_source/real.pdf',
	output:
		'week_2/handout_2.pdf'
	shell:
		"""
		cd week_2/handout_source && pdflatex handout_2.tex && bibtex handout_2.aux && pdflatex handout_2.tex && pdflatex handout_2.tex && cp handout_2.pdf ../
		"""

rule handout_2_plots:
	input:
		'week_2/handout_source/plots.py',
	output:
		'week_2/handout_source/x_squared.pdf',
		'week_2/handout_source/real.pdf'
	shell:
		"""
		cd week_2/handout_source && python plots.py && cd ../../
		"""

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
