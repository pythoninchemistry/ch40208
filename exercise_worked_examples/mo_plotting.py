"""Functions for plotting the molecular orbitals of conjugated pi-systems"""

from scipy.special import sph_harm
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi,101)
colours = {'+ve': 'darkorange',
           '-ve': 'deepskyblue',
           'outline': 'darkslategrey'}

def plot_p_orbital(ax, origin, scaling=1.0):
    """Plot a single p-orbital.
    
    Args:
        ax (axis): matplotlib axis to plot onto.
        origin (np.array): length 2 numpy array specifying the
            (x,y) coordinates for this p-orbital.
        scaling (float, optional): Optional scaling factor for plotting
            this p-orbital. Default is 1.0
            
    Returns:
        None
        
    """
    theta = np.linspace(0,2*np.pi,101)
    r = np.real(sph_harm(-2,2,0,theta)) * scaling
    x = r*np.cos(theta) + origin[0]
    y = r*np.sin(theta) + origin[1]
    ax.plot(x, y, c=colours['outline'])
    ax.fill(x[:51],y[:51], c=colours['+ve'], alpha=1.0)
    ax.fill(x[51:],y[51:], c=colours['-ve'], alpha=1.0)

def plot_linear_mo(coefficients, spacing=0.35, show=True):
    """Plot a molecular orbital for a linear conjugated pi-system
    
    Args:
        coefficients (list(float)): list of coefficients for each
            p-orbital in this molecular orbital,
            e.g. [0.3, 0.7, -0.7, -0.3]
        spacing (float, optional): Optional spacing between each p-orbital.
            Default is 0.35
        show (bool, optional): Set whether to show the figure.
            Default is True
            
    Returns:
        None
        
    """
    fig = plt.figure()
    ax = fig.add_subplot(111,aspect='equal')
    for i, c in enumerate(coefficients, 1):
        x = i*spacing
        y = 0.0
        plot_p_orbital(ax, [x,y], c)
    plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,
    right=False,
    labelbottom=False,
    labelleft=False)
#     fig.patch.set_visible(False)
    ax.axis('off')
    if show:
        plt.show()
    
    
def plot_cyclic_mo(coefficients, show=True):
    """Plot a molecular orbital for a cyclic conjugated pi-system
    
    Args:
        coefficients (list(float)): list of coefficients for each
            p-orbital in this molecular orbital,
            e.g. [-0.7, 0.7, -0.7, 0.7]
        show (bool, optional): Set whether to show the figure.
            Default is True
            
    Returns:
        None
        
    """
    n_points = len(coefficients)
    alpha = np.arange(n_points)*np.pi*2.0/n_points + np.pi/2 
    if n_points%2 == 0:
        alpha = alpha + np.pi/n_points
    r = 1
    x = r*np.cos(alpha)
    y = r*np.sin(alpha)
    fig = plt.figure()
    ax = fig.add_subplot(111,aspect='equal')
    ax.plot(x,y, c='grey', linestyle='--')
    scaling = 8/n_points**0.7
    ax.plot([x[-1],x[0]], [y[-1], y[0]], c='grey', linestyle='--')
    for x_p, y_p, c in zip(x, y, coefficients):
        plot_p_orbital(ax, [x_p,y_p], c*scaling)
    plt.tick_params(
        axis='both',       # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False)
#     fig.patch.set_visible(False)
    ax.axis('off')
    if show:
        plt.show()