HANDOUTS = ['week_4/handout_4.pdf']

rule all:
	input:
		HANDOUTS,
		'week_4/mini.mp4'

rule handout_4:
	input:
		'week_4/handout_source/handout_4.tex',
	output:
		'week_4/handout_4.pdf'
	shell:
		"""
		cd week_4/handout_source && pdflatex handout_4.tex && pdflatex handout_4.tex && cp handout_4.pdf ../
		"""

rule mini:
	input:
		'week_4/plots.py',
	output:
		'week_4/mini.mp4'
	shell:
		"""
		python week_4/plots.py
		ffmpeg -y -framerate 2 -i week_4/mini/%01d.png -pix_fmt yuv420p week_4/mini.mp4
		"""
