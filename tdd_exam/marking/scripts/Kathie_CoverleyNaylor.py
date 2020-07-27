# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):

    """
    To determine the pressure of a system using the ideal gas law
    
    args:
    number_of_moles- (float): No of moles of gas in a given system
    temperature (float): Temperature of the system (units of K)
    volume (float): Volume of system (units of m3)
    
    returns: pressure of the system (in Pascals)
    """
    
    if temperature < 0:
        raise ValueError ("Temperature cannot be below 0K")
    
    if number_of_moles < 0:
        raise ValueError ("Number of moles cannot be less than 0")
    
    if volume < 0:
        raise ValueError ("Pressure cannot be less than 0")
        
    return ((number_of_moles * R * temperature)/ volume)


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    
    """
    Determines allowed vibrational transitions
    
    Args:
    v_0 - ground vibrational energy state
    v_1 - first vibrational energy state
    
    returns under conditions that:
    v_0/v_1 are not negative
    v_1 = +/- v_0
    both values are integers
    
    """
    
    if v_0 <= 0: 
        raise ValueError("Ground state vibrational energy cannot be less than zero")
    if v_1 <= 0: 
        raise ValueError("Vibrational energy 1 cannot be less than zero")
    if v_0 and v_1 <=0 :
        raise ValueError("Vibrational energy 1 cannot be less than zero")
    if not isinstance(v_0, int):
        raise TypeError("Value must be an integer")
        
    if not isinstance(v_1, int):
        raise TypeError("Value must be an integer")
    
    if v_1 != (v_0 - 1) or v_1 != (v_0 + 1):
        
             raise ValueError("Value must be +/- 1 fpr transition to be allowed") 
    
    return np.arange(v_0, v_1)
     

# Function for coulomb

import numpy as np

from scipy.constants import epsilon_0


def coulomb(r, q_i, q_j):

    """
    Determines the potential energy between charged particles 
    Args: 
    r = seperation between particles, can be an array or float depending on 
    whether list of r values or single value is given.
    q_i (int)- charge of Li+ ion 
    q_j (int)- charge of O2- anion 
    """
    
    if not isinstance(q_j, int):
        raise TypeError("Value must be an integer")
    if not isinstance(q_i, int):
        raise TypeError("Value must be an integer")
    
    return ((q_i*q_j)/ ((4 * np.pi) * epsilon_0 * r))
    #else:
     #   array_r = np.array([r])  
    
   # return ((q_i*q_j)/ ((4 * np.pi) * epsilon_0 * array_r))
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    The goodness-of-fit metric between the model 
    and experimental data. 
    """
    
    
    chi_squared = np.sum(np.square((
        model - exp) / exp_uncertainty))
    
    return chi_squared
    


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determines rotational contribution to the total partition function from the first 
    N energy levels.
    args:
    rotational constant B float
    Temperature- float, Kelvin
    N- number of energy levels
    returns rotational contribution 
 
    """
    
    N = np.array[(0, 1, 2, 3, 4, 5, 6, 7)]
    
    return np.sum ((2*N) + 1)* np.exp (-h * c * rotational_constant * N * (N+1)/ (k* temperature))








