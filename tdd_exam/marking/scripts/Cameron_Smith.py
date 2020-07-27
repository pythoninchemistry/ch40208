# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the pressure of a system from the number of moles, temperature and pressure of the system using
    the ideal gas law.
    
    Args:
    number_of_moles (float): The number of moles in the system. (mol)
    temperature (float): The temperature of the system. (K)
    volume (float): The volume of the system. (dm^3)
    
    Returns:
    pressure (float): The pressure of the system (Pa)
    """
    if temperature < 0:
        raise ValueError('The temperature must be greater than or equal to 0 K')
    elif number_of_moles < 0:
        raise ValueError('The number of moles must be greater than or equal to 0 mol')
    elif volume < 0:
        raise ValueError('The volume must be greater than or equal to 0 Pa')
    else:
        pressure = (number_of_moles * R * temperature) / volume
        return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines if a transition between 2 quantum states is allowed, and returns a Boolean value of True or False.
    
    Args:
    v_0 (int): The original vibrational energy level
    v_1 (int): The final vibrational energy level
    
    Returns:
    True or False (bool): A boolean value of True of False depending on if the transition is allowed or not respectively.
    """
    if not isinstance(v_0, int):
        raise TypeError('The original vibrational energy level must be an integer.')
    elif not isinstance(v_1, int):
        raise TypeError('The final vibrational energy level must be an integer.')
    elif v_0 < 0:
        raise ValueError('The original vibrational energy level must be greater than or equal to 0.')
    elif v_1 < 0:
        raise ValueError('The final vibrational energy level must be greater than or equal to 0.')
    elif v_0 - v_1 == 1:
        return True
    elif v_1 - v_0 == 1:
        return True
    elif not v_1 - v_0 == 1:
        return False
    elif not v_0 - v_1 == 1:
        return False
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Finds the potential energy between two charged particles i and j at separation r with charges q_i and q_j respectively.
    
    Args:
    r (float) or (list): The distance between the charged particles. Can take a single float value or a list, as long
                         as the charges q_i and q_j remain constant.(m)
    q_i (int): The charge on particle i.
    q_j (int): The charge on particle j.
    
    Returns:
    potential energy (float) or (list): The potential energy between the two charged particles at given r value(s). (J)
    """
    if not isinstance(q_i, int):
        raise TypeError('The charge on particles must be an integer.')
    elif not isinstance(q_j, int):
        raise TypeError('The charge on particles must be an integer.')
    elif isinstance(r, int):
        potential_energy = (q_i * q_j) / (4 * np.pi * epsilon_0 * r)
    elif isinstance(r, list): 
        potential_energy = []
        for distances in r:
            potential_energy = potential_energy + [((q_i * q_j) / (4 * np.pi * epsilon_0 * distances))]
        
    return potential_energy
    
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Finds the goodness of fit parameter between model and experimental data.
    
    Args:
    model (np.array): A numpy array of model data
    exp (np.array): A numpy array of experimental data
    exp_uncertainty (np.array): A numpy array of uncertainty in experimental data
    
    Returns:
    goodness_of_fit: (float): The goodness of fit parameter for the given data.
    
    """
    if not len(model) == len(exp) == len(exp_uncertainty):
        raise ValueError('All data sets must be the same length.')
    else:
        goodness_of_fit = np.sum(np.square((model - exp) / exp_uncertainty))
    return goodness_of_fit



# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Finds the rotational contribution from a given N, rotational constant and temperature.
    
    Args:
    N (int): The number of energy levels
    rotational_constant (float): The rotational constant (cm^-1)
    temperature (float): The temperature of the system (K)
    
    Returns:
    rotational_contribution_total (float): The total rotational contribution summed over N values.
    """
    if not isinstance (N, int):
        raise TypeError('N must be an integer!')
    elif rotational_constant < 0:
        raise ValueError('The rotational constant must be greater than or equal to 0 cm^-1.')
    elif temperature < 0:
        raise ValueError('The temperature must be greater than or equal to 0 K.')
    for J in range (0, N+1):
        rotational_contribution_total = []
        rotational_contribution = (2 * (J + 1)) * np.exp((- h * c * rotational_constant * J * (J + 1)) / k * temperature)
        rotational_contribution_total = rotational_contribution_total + rotational_contribution

        return rotational_contribution_total