# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the pressure of an ideal gas from the number of moles, 
    temperature and volume using the ideal gas law"
    
    Args:
        number_of_moles (float): the number of moles of the ideal gas
        temperature (float):the temperature of the system in Kelvin
        volume (float): the volume of the gas in cubic decimetres
    
    Returns:
        float: gas pressure (Pa)
    """
    
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    else: 
        return (number_of_moles * R * temperature)/volume

    if number_of_moles < 0:
        raise ValueError("The number of moles is unphysical (n < 0).")
    else: 
        return (number_of_moles * R * temperature)/volume
    
    if volume < 0:
        raise ValueError("The volume is unphysical (V < 0)")
    else: 
        return (number_of_moles * R * temperature)/volume
                          
    return (number_of_moles * R * temperature)/volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether or not a transition between vibrational
    energy levels is allowed by the vibrational selection rule"
    
    Args:
        v_0 (int): the vibrational quantum number for the initial state
        v_1 (int): the vibrational quantum number for the final state
    
    Returns: Boolean (true or false)
                If True, the transition is allowed. If False, the
                transition is  forbidden.
    """
    if (v_1 - v_0) != 1: 
        raise ValueError("The transition is forbidden") 
    else:
         return (v_1 - v_0)
        
    if (v_1 - v_0) != (-1):
        raise ValueError("The transition is forbidden")
    else:
        return (v_1 - v_0)     
    if (v_1 - v_0) > 1:
        raise ValueError("The transition is forbidden")
    else:
        return (v_1 - v_0)
   
    return (v_1 - v_0)
   

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    
    return 
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    
    return 


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    
    return 