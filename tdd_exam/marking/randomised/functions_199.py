# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determines the pressure of an ideal gas
    
    Args:
        number_of_moles (float): the number of moles of the gas in the system
        temperature (float): the temperature of the system in kelvin
        volume (float): the volume of the system in m^3
    Returns:
        float: the pressure of the system in pascals
    """
    if temperature < 0:
        raise ValueError('Temperature value given is unphysical')
    if number_of_moles < 0:
        raise ValueError('Moles value given is unphysical')
    if volume < 0:
        raise ValueError('Volume value given is unphysical')
        
    return (number_of_moles * R * temperature)/ volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether the vibrational energy level transition is allowed or not
    
    Args:
        v_0 (int): the initial vibrational energy level
        v_1 (int): the final vibrational energy level
    Returns:
        Boolean: True or False whether transition follows selection rules and is allowed
    """
    if v_0 + 1 == v_1 or v_0 - 1 == v_1:
        allowed = True
    else:
        allowed = False
    if type(v_0) != int:
        raise TypeError('initial vibrational energy level must be an integer')
    if type(v_1) != int:
        raise TypeError('final vibratonal energy level must be an integer')
    if v_0 < 0:
        raise ValueError('initial vibrational energy level must be greater'
                         'than or equal to zero')
    if v_1 < 0:
        raise ValueError('final vibrational energy level must be greater than'
                         'or equal to zero')
    return allowed
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Determines the potential energy between two charged particles at a given separation
    
    Args:
        r (float): separation distance of the two particles
        q_i (int): charge on particle i
        q_j (int): charge on particle j
    Returns:
        float: potential energy between the two particles
    """
    if type(r) != int:
        r = np.array(r)
        for i in r:
            V = (q_i * q_j)/(4 * np.pi * epsilon_0 * r)
    else:
        V = (q_i * q_j)/(4 * np.pi * epsilon_0 * r)
    
    return V
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the sum of the squared differences between experimental data
    and model data
    
    Args:
        model (float, array): data points from the model 
        exp (float, array): data points from the experimental
        exp_uncertainty (float, array): uncertainty of the data from experimental
    Returns:
        float: sum of the squared differences
    """
    chi = np.sum(((exp - model)/exp_uncertainty)**2)
    
    if len(model) != len(exp) and len(exp_uncertainty):
        raise ValueError('the number of data points for the model must be equal'
                         'to experimental and experimental uncertainty')
    if len(exp) != len(model) and len(exp_uncertainty):
        raise ValueError('the number of data points for experimental must be equal'
                         'to model and experimental uncertainty')
    if len(exp_uncertainty) != len(model) and len(exp):
        raise ValueError('the number of data points for experimental uncertainty'
                         'must be equal to model and experimental')
    
    return chi


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution to the molecular partition function for
    the first N energy levels
    
    Args:
        N (int): the number of energy levels
        rotational_constant (float): rotational constant for the molecule
        temperature (float): the temperature in Kelvin
    Returns:
        float: the rotational contribution to the molecular partition function
    """
    j = np.arange(0,N+1)
    q = np.sum((2*j + 1) * np.exp((-h * (c*100) * rotational_constant * j * (j+1))/ (k * temperature)))
    if rotational_constant < 0:
        raise ValueError('rotational constant must be greater than or equal to zero')
    if temperature < 0:
        raise ValueError('temperature is unphysical, must be greater than or equal to zero')
    if type(N) != int:
        raise TypeError('the number of energy levels must be an integer')
        
    return q