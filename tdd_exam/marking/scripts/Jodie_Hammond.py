# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    if temperature < 0:
        raise ValueError('The temperature must be greater than 0')

    if number_of_moles < 0:
        raise ValueError('The number of moles must be greater than 0')

    if volume < 0:
        raise ValueError('The volume must be greater than 0')
    return (number_of_moles * R * temperature) / volume 


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):    
    if v_0 != int:
        return TypeError('v0 must be an integer')
        
    if v_1 != int:
        return TypeError('v0 must be an integer')
        
    if v_0 < 0:
        return ValueError('v0 must be greater than 0')
        
    if v_1 < 0:
        return ValueError('v1 must be greater than 0')
        
    if v_1 + v_0 != 1 or -1:
        return False
    
    if v_1 - v_0 != 1 or -1:
        return False
        
    if v_0 + v_1 != 1 or -1:
        return False
        
    if v_0 - v_1 != 1 or -1:
        return False
    
    else:
        return True
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    if r < 0:
        raise ValueError('The seperation must be greater than 0')
        
   
    
    return ((q_i * q_j) / (4 * np.pi * epsilon_0 * r))
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty): 
    #if np.array(model) != np.array(exp) != np.array(exp_uncertainty):
        #raise ValueError('Data arrays must be of the same length')
    
    chi_squared = np.sum(np.square((model - exp) / exp_uncertainty))
    return chi_squared



# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    if N != int:
        return TypeError('N must be an integer')
    
    if rotational_constant < 0:
        return ValueError('B must be greater than 0')
    
    if temperature < 0:
        return ValueError('T must be greater than 0')
        
    return np.sum((2 * N) + 1) * np.exp * (-h * c * (rotational_constant / 100) * (N * (N + 1)) / k * temperature)
    
    
    
    
    
    

    
    