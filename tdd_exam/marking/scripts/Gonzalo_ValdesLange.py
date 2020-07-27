# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determines the pressure of an ideal gas given 3 variables
    
    Args:
        number of moles (float) in moles
        temperature (float, in kelvin)
        volume (float) in m^3
        
    Returns:
        float: pressure of the gas
    """
    if number_of_moles <= 0:
        raise ValueError ('number of moles cannot be less than zero')
    elif temperature <= 0:
         raise ValueError ('temperature cannot be less than zero')
    elif volume <= 0:
         raise ValueError ('volume of gas cannot be less than zero')
            
    return (number_of_moles * R * temperature) / volume

# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines the vibrational transition difference between final 
                              and initial energy levels
    
    Args:
        inital energy level (int) no units
        final energy level (int) no units
        
    Returns:
        int/boolean: difference between energy levels and whether the transition is allowed
    """
    if (v_1 - v_0 == -1) or (v_1 - v_0 == 1):    
        if v_0 <=0:
            raise ValueError ('the starting quantum state has to be greater than 0 ')
        elif not isinstance (v_0, int):
            raise TypeError ('the starting quantum state has to be an integer ')     
        elif v_1 <=0:
            raise ValueError ('the final quantum state has to be greater than 0 ')
        elif not isinstance (v_1, int):
            raise TypeError ('the final quantum state has to be an integer ') 

        return True
    
    if (v_1 - v_0 != -1) or (v_1 - v_0 != 1):
        return False
    if (v_1 - v_0 != -1) or (v_1 - v_0 != 1):
        raise ValueError ('the difference in vibrational energies is more' 
                                        ' than 1') 
    
# Function for coulomb
from scipy.constants import epsilon_0
from math import pi

def coulomb(r, q_i, q_j):
    """
    Determines potential energy given distance and charges
    
    Args:
        r is distance (float)
        q_i is a charge (int)
        q_j is a charge (int)
        
    Returns:
        float: potential energy 
    """
    
    return (q_i * q_j)/(4 * pi * epsilon_0 * r)

   
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the sum of squared difference between model and experimental data
    
    Args:
        model (float) 
        exp (float)
        exp_uncertainty (float) 
        
    Returns:
        float: sum of squared difference
    """
    return np.sum(np.square((exp-model/exp_uncertainty)**2))

# Function for partition
from scipy.constants import h, c, k
import numpy as np
from math import exp

def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution
    
    Args:
        N (array-like, interger), number of energies
        rotational_constant (float) in cm^-1
        temperature (float) in Kelvins
        
    Returns:
        float: rotational contribution
    """
    if T <=0:
            raise ValueError ('the starting quantum state has to be greater than 0 ')
        elif not isinstance (N, int):
            raise TypeError ('the starting quantum state has to be an integer ')     
    Jlist = []
    for J in range(0, N):
        Jlist.append(2 * J + 1) * exp (-h * c * 100 * rotational_constant * J * (J + 1) /(k * temperature))

    return np.sum(Jlist)

