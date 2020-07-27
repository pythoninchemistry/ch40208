# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    This function determines and returns the 
    pressure of an ideal gas.
    
    Args: 
        number_of_moles (float): The  number of moles of gas in the system. 
        temperature (float): The temperature of the gas in the system (K).
        volume (float): The volume that the gas occupies in the system (m^3)
        
    Returns: 
        float: The pressure of the gas in the system (Pa). 
    """
    if temperature < 0:
        raise ValueError('The Temperature is unnphysical (T<0).')
    if number_of_moles < 0:
        raise ValueError('The number of moles is unphysical (n < 0).')
    if volume < 0:
        raise ValueError('The volume is unphysical (V < 0 m^3)')
        
    return (number_of_moles * R * temperature) / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    This function determines whether transitions between
    inital and final vibrational levels are allowed or not.
    
    Args:
        v_0 (int): The initial vibrational energy level.
        v_1 (int): The final vibrational energy level. 
        
    Returns:
        Boolean: Whether the transition is allowed or not. (True/False)
    """
    if type(v_0) != int:
        raise TypeError('The initial vibrational energy level must be an integer.')
    if type(v_1) != int:
        raise TypeError('The final vibrational energy level must be an integer.')
    if v_0 < 0:
        raise ValueError('The intial vibirational energy level must be greater or equal to 0.')
    if v_1 < 0:
        raise ValueError('The final vibration energy level must be greater or equal to 0.')
    if (v_0 - v_1) == 1 or (v_0 - v_1) == -1:
        return True
    else:
        return False
    


# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    This function should return return the potential energy of 
    two charged particles given a distance, 'r'.
    
    Args: 
        r(float): The separation between the two particles.
        q_i (int): The relative charge of particle i.
        q_j (int): The relative charge of particle j.
        
    Returns:
        float: The potential energy between particles i and j. 
    """
    R = np.array(r)
    A  =  (q_i * q_j) / (4 * np.pi * epsilon_0 * r)
    return A
    
        
    
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    This function returns a value of chi squared
    given an experimental data set. 
    
    Args: 
        model(array_like, float): model data set.
        exp(array_like, float): experimental data set.
        exp_uncertainty(array_like, float): Uncertainty in the experimental data set.
        
    Returns:
        array_like, float: The value of chi squared from the experimental data set. 
    
    """
    if len(model) != len(exp) and len(model) == len(exp_uncertainty):

        return np.sum(((exp - model) / exp_uncertainty)**2) 
    else:
        raise ValueError('The amount of data is not the same as in the arrays listed.')

# Function for partition
from scipy.constants import h, c, k
def partition(N, rotational_constant, temperature):
    """
    This function should determine the rotational contribution
    to the molecular partition function.
    
    Args: 
        N(int):The corresponding energy level.
        rotational_constant(float): The value of the rotational constant (cm^-1). 
        temperature(float): The temperature of the system (K).
    
    Returns: The rotational contribution to the molecular partition function, 'q^R'.
        
    """
    if not isistance(N, int): 
        raise TypeError('N should be an integer.')
    if rotational_constant < 0:
        raise ValueError('The value for the rotational constant is unphysical (<0).')
    if temperature < 0:
        raise ValueError('The Temperature is unphysical (<0 K).')
    
    energy_values = np.arange(N+1)
    
    total_energy = ((2*energy_values) + 1) * np.exp(-h * c * rotational_constant * energy_values * (energy_values + 1) / (k * temperature))
    
    return np.sum(total_energy)