# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    
    if temperature < 0:
        raise ValueError('The temperature must be greater than 0K')
    elif number_of_moles < 0:
        raise ValueError('The number of moles must be greater than 0')
    elif volume < 0:
        raise ValueError('The volume must be greater than 0')
    else:
        return ((number_of_moles * R * temperature) / volume) 

     


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    if v_0 <= 0:
        raise ValueError('The value of v0 must be a positive number')
    if v_1 <= 0:
        raise ValueError('The value of v1 must be a positive number')
    if type(v_0) == float:
        raise TypeError('The value for v0 must be an integer')
    if type(v_1) == float:
        raise TypeError('The value for v1 must be an integer')
    elif (v_0 - v_1) == 1:
        return True
    elif (v_1 - v_0) == 1:
        return True
    elif (v_0 - v_1) == -1:
        return True
    elif (v_1 - v_0) == -1:
        return True
    elif (v_0 - v_1) != 1:
        return False
    
     
     

# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    if type(r) == int:
        return ((q_i * q_j)/(4 * pi * epsilon_0 * r))
    else: 
        result = []
        for n in r:
            result.append(((q_i * q_j)/(4 * pi * epsilon_0 * n)))
        return result
    
        
    
    
    
    
     
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    if np.shape(exp) != np.shape(model):
        raise ValueError('The exp array has too few values')
    if np.shape(model) != np.shape(exp):
        raise ValueError('The model array has too few values')
    if np.shape(exp_uncertainty) != np.shape(model):
        raise ValueError('The exp_uncertainty array has too few values')
 


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    if type(N) == float:
        raise TypeError('N must be an integer')
    if rotational_constant < 0:
        raise ValueError('B must be greater than 0')
    if N < 0:
        raise ValueError('N must be greater than 0')
    if temperature < 0:
        raise ValueError('T must be greater than 0')