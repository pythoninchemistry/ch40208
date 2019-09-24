HANDOUTS = ['week_3/handout_3.pdf']

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
