# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, pressure):
    """
    A function to calculate the volume of an ideal gas
    
    Parameters:
    number_of_moles : the number of moles in the volume
    temperature : the temperature of the sytsem in Kelvin
    pressure : the pressure of the system in Pascals
    
    return:
    (number_of_moles * R * Temperature) / pressure
    """
    if temperature < 0:
        raise ValueError('Temperature must be greater than 0K')
    elif number_of_moles < 0:
        raise ValueError('The number of moles must be greater than 0')
    elif pressure < 0:
        raise ValueError('The pressure of the system has to be greater than 0 Pa')
    else:
        return (number_of_moles * R * temperature) / pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    A function to determine if a transition is allowed or not
    
    parameters:
    v_0 : the vibrational energy level of the original
    v_1 : the vibrational energy level of the excited
    
    return:
    delta_v = v_1 - v_0
    """
    delta_v = v_1 - v_0
    if v_0 < 0:
        raise ValueError('The vibrational energy levels have to be positive')
        
    elif v_1 < 0:
        raise ValueError('The vibrational energy levels have to be positive')
    
    elif v_1 != int(v_1) or v_0 != int(v_0):
        raise TypeError('The vibrational energy levels have to be integers')
    
    else:
        if delta_v == 1 or delta_v == -1:
            return bool(True)
    
        elif delta_v > 1 or delta_v < -1:
            return bool(False)
    
    
    
    
    
    
    
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    a fuction to calculate the separation between 2 charged particles
    of spearation r 
    
    parameters:
    r : distance betweeen particles
    q_i : charge of particle i
    q_j : charge of particle j
    epsilon_0 : permittivity in a vacuum
    
    return:
    (q_i * q_j) / (4 * np.pi * epsilon_0 * r)
    """
    if r == list(r):
        for rs in r:
            return (q_i * q_j) / (4 * np.pi * epsilon_0 * rs)
    else:
        return (q_i * q_j) / (4 * np.pi * epsilon_0 * r)
           
          
    
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    A function to determine the chi squared value
    
    parameters:
    model : value for the model
    exp : value for the experiment
    exp_uncertainty : experimental uncertainty in exp
    
    Return:
    np.sum(((model * exp) / exp_uncertainty) ** 2)
    """
    if len(model) != len(exp) or len(model) != len(exp_uncertainty) or len(exp) != len(exp_uncertainty):
        raise ValueError('The lengths of your arrays are not the same')
        
    else:
        return np.sum(((exp[:3] - model[:3]) / exp_uncertainty[:3])**2)


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    A fuction to calculate the rotational contibution to a molecular function
    
    Parameters:
    N : number of energy levels
    rotational_constant : the rotational constant for the molecule
    temperature : the temperature in Kelvin
    
    return:
    np.sum(((2 * J) + 1) * np.exp((h * c *rotational_constant * J (J+1))/k * temperature)) 
    """
    if N != int(N):
        raise TypeError('N has to be an integer value')
    
    elif rotational_constant < 0:
        raise ValueError('B has to be greater than 0')
    
    elif temperature < 0:
        raise ValueError('temperature has to be greater than 0K')
        
    else:
        for J in range(0, N, 1):
            return np.sum((2*J + 1) * np.exp(((-h * c * (rotational_constant / 100) * J * (J+1))/(k *temperature)))) 