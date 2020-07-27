# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    '''
    This finds the pressure of an ideal gas
    
    Args:
       number_of_moles (int): Number of moles of gas in system
       temperature: Temperature of system
       Volume (float): Volume of gas in system
       
    Returns:
       float: Pressure of gas in system (Pa)
       
    '''

    if temperature < 0:
        raise ValueError('The temperature is unphysical (T < 0).')
    if number_of_moles < 0:
        raise ValueError('The number of moles is unphysical.')
    if volume < 0:
        raise ValueError('The volume is unphysical.')
    return (number_of_moles * R * temperature) / volume

# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    '''
    This describes whether a vibrational transition is allowed or not
    
    Args:
       value (int): Initial vibrational energy level
       value (int): Final vibrational energy level
       
    Returns:
       boolean: True if allowed, false if not allowed
       
    '''
    if v_0 - v_1 > 1:
        return False
    if v_1 - v_0 > 1:
        return False
    if v_0 < 0:
        raise ValueError ('Vibrational energy levels must be int >= 0')
    if v_1 < 0:
        raise ValueError ('Vibrational energy levels must be int >= 0')
    if v_0 == float:
        raise TypeError ('Vibrational energy levels must be int >= 0')
    if v_1 == float:
        raise TypeError ('Vibrational energy levels must be int >= 0')
    else:
        return True
    
# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    '''
    This describes the potenetial energy between two charged particales
    
    Args:
       value (int): Seperation between particles
       value (int): Charge on one particle
       value (int): Charge on the other particle
       
    Returns:
       float: Potential energy
    '''
    return (q_i * q_j) / (4 * np.pi * epsilon_0 * np.array(r))
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    '''
    This function reduces the sum of th squared difference
    between the experimental data and the model
    
    Args:
       model (array_like, float): The model
       exp (array_like, float): Experimental values
       exp_uncertainity (array_like, float): Uncertainity on experimental values
       
    Returns:
       float: goodness-of-fit parament (chi2)
    '''
    if len(model) != len(exp):
        raise ValueError('The lengths of the arrays of variables have to be the same')
    return np.sum(((exp - model) / exp_uncertainty) ** 2)
                  
                  
              
# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    '''
    This describes the rotational contribution to the molecular partition function
    
    Args:
       N (int): Upper limit of J values to been summed over
       rotational_constant (float): The rotational constant (B)
       temperature (float): Temperature in K
       
    Returns:
       float: rotational contribution to molecular partition function
    '''    
    if N == float:
        raise TypeError('N has to be an integer')
    if rotational_constant < 0:
        raise ValueError('B is unphysical')
    if temperature < 0:
        raise ValueError('Temperature is unphysical')
    a = np.arange(0, N+1)
    #return np.sum((2 * a + 1) * np.exp((-h * c * rotational_constant * a * (a + 1)) / (k * temperature)))           