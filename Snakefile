HANDOUTS = ['week_1/handout_1.pdf', 'week_2/handout_2.pdf', 'week_3/handout_3.pdf', 'week_4/handout_4.pdf', 'week_5/handout_5.pdf', 'data_analysis/handout.pdf', 'week_8/handout_8.pdf', 'week_9/handout_9.pdf']

rule all:
	input:
		HANDOUTS,
    	'week_3/mini3.mp4',
    	'week_3/mini4.mp4',

rule data_analysis:
	input:
		'data_analysis/handout_source/handout.tex',
	output:
		'data_analysis/handout.pdf'
	shell:
		"""
		cd data_analysis/handout_source && pdflatex handout.tex && pdflatex handout.tex && cp handout.pdf ../
		"""

rule handout_9:
	input:
		'week_9/handout_source/handout_9.tex',
                'week_9/figures/ellipse_major_minor_axes_transformation.pdf',
                'week_9/figures/matrix_transformation_unit_circle.pdf',
                'week_9/figures/matrix_transformation.pdf',
	output:
		'week_9/handout_9.pdf'
	shell:
		"""
		cd week_9/handout_source && pdflatex handout_9.tex && pdflatex handout_9.tex && cp handout_9.pdf ../
                """	

rule handout_8:
	input:
		'week_8/handout_source/handout_8.tex',
                'week_8/figures/position_vectors_1.pdf',
                'week_8/figures/position_vectors_2.pdf',
                'week_8/figures/position_vectors_3.pdf',
                'week_8/figures/position_vectors_4.pdf',
                'week_8/figures/cross_product.pdf',
                'week_8/figures/position_vectors_alternate_basis.pdf',
                'week_8/figures/rotation_example.pdf',
                'week_8/figures/vector_addition.pdf',
	output:
		'week_8/handout_8.pdf'
	shell:
		"""
		cd week_8/handout_source && pdflatex handout_8.tex && pdflatex handout_8.tex && cp handout_8.pdf ../    
		"""

rule handout_5:
	input:
		'week_5/handout_source/handout_5.tex',
	output:
		'week_5/handout_5.pdf'
	shell:
		"""
		cd week_5/handout_source && pdflatex handout_5.tex && pdflatex handout_5.tex && cp handout_5.pdf ../
    	"""

rule handout_4:
	input:
		'week_4/handout_source/handout_4.tex',
	output:
		'week_4/handout_4.pdf'
	shell:
		"""
		cd week_4/handout_source && pdflatex handout_4.tex && pdflatex handout_4.tex && cp handout_4.pdf ../
    	"""

rule handout_3:
	input:
		'week_3/handout_source/handout_3.tex',
		'week_3/handout_source/dihedral.pdf',
	output:
		'week_3/handout_3.pdf'
	shell:
		"""
		cd week_3/handout_source && pdflatex handout_3.tex && pdflatex handout_3.tex && cp handout_3.pdf ../
		"""

rule mini3:
	input:
		'week_3/plots.py',
	output:
		'week_3/mini3.mp4'
	shell:
		"""
		python week_3/plots.py
		ffmpeg -y -framerate 2 -i week_3/mini3/%01d.png -pix_fmt yuv420p week_3/mini3.mp4
    	"""

rule mini4:
	input:
		'week_3/plots.py',
	output:
		'week_3/mini4.mp4'
	shell:
		"""
		python week_3/plots.py
		ffmpeg -y -framerate 2 -i week_3/mini4/%01d.png -pix_fmt yuv420p week_3/mini4.mp4
    	"""

rule handout_3_plots:
	input:
		'week_3/handout_source/dihedral_plot.py',
	output:
		'week_3/handout_source/dihedral.pdf',
	shell:
		"""
		cd week_3/handout_source && python dihedral_plot.py && cd ../../
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
		cd week_2/handout_source && pdflatex handout_2.tex && bibtex handout_2.aux && pdflatex handout_2.tex && pdflatex handout_2.tex && pdflatex handout_2.tex && cp handout_2.pdf ../
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
