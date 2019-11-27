import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 18})

def xyz_projections(coords):
    """
    Plot the projected atom coordinates along the
    x, y, and z axes.
    
    Args:
        coords (np.array): Nx3 numpy array of atomic coordinates.
        
    Returns:
        None
        
    """
    fig, ax = plt.subplots(1,3, sharex=True, sharey=True, 
                           subplot_kw={'aspect':'equal'}, figsize=(12,8))
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[0].set_title('z')
    
    ax[1].set_xlabel('z')
    ax[1].set_ylabel('y')
    ax[1].set_title('x')
    
    ax[2].set_xlabel('z')
    ax[2].set_ylabel('x')
    ax[2].set_title('y')
    ax[0].plot(coords[:,1], coords[:,2], 'o', markersize=30, clip_on=False)
    ax[1].plot(coords[:,0], coords[:,2], 'o', markersize=30, clip_on=False)
    ax[2].plot(coords[:,0], coords[:,1], 'o', markersize=30, clip_on=False)
    for i in range(2):
        ax[i].set_xticks([-1,0,1])
        ax[i].set_yticks([-1,0,1])
    fig.tight_layout()
    fig.show()
