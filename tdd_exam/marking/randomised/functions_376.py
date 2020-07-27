# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    
    """calculates pressure of an ideal gas provided the number of moles
    temperature and volume. Raises value errors if unphysical values are inputted
    args: 
    number_of_moles = number of moles of an ideal gas in the system
    temperature = temperature of the gas in Kelvin
    volume = volume of the gas in cubic metres"""
    
    pressure = ((number_of_moles*temperature*R)/volume)
    if temperature < 0:
        raise ValueError('unphysical temperature')
    elif number_of_moles < 0:
        raise ValueError('unphysical number of moles')
    elif volume < 0:
        raise ValueError('unphysical volume')
    else:
        return pressure
    

# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    
    """determines whether a given vibrational transition is allowed
    raises errors if values other than positive integers are inputted
    args:
    v_0 = initial vibrational energy level
    v_1 = end vibrational energy level
    """
    
    if(v_1 - v_0) == 1 or -1:
        return True
    elif v_0 or v_1 < 0:
        raise ValueError('negative quantum numbers are not permitted')
    elif (type(v_1)== int) or (type (v_2) == int) == False:
        raise TypeError('non-integer quantum numbers are not permitted')
    else:
        return False

    
     

# Function for coulomb
from scipy.constants import epsilon_0
from math import pi
def coulomb(*r, q_i, q_j):
    """
    calculates the coulombic potential energy of a system containing two ions of separation r
    args:
    r = separation of charges in metres
    q_i = charge of one ion
    q_j = charge of the other ion
    """
    potential_energy = (q_i * q_j)/(4* pi * epsilon_0 * r)
    
    return potential_energy
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    
    return 


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    
    return 