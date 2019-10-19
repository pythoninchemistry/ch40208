import matplotlib.pyplot as plt


def show(x, y):
    """
    Enables the visiualisation of the water
    molecule

    Parameters 
    ----------
    x : x-positions for molecule
    y : y-positions for molecule 
    """
    marks = [r'$O$', r'$H$', r'$H$']
    plt.figure(figsize=(5, 5))
    for i in range(len(x)):
        plt.plot(x[i], y[i], marker=marks[i], ms=20, zorder=10)
    reorderx = [x[1], x[0], x[2]]
    reordery = [y[1], y[0], y[2]]
    plt.plot(reorderx, reordery, 'k-')
    plt.yticks([])
    plt.xticks([])
    plt.ylim([-2, 2])
    plt.xlim([-2, 2])
    plt.show()