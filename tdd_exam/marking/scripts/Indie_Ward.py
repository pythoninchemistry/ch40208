# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the pressure of an ideal gas using the Ideal Gas Law.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        volume (float): Volume occupied by the ideal gas (m^3).
    
    Returns:
        float: pressure of the ideal gas (Pa).
    """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if number_of_moles < 0:
        raise ValueError("The number of moles is unphysical ( n < 0 mol).")
    if volume < 0:
        raise ValueError("The volume of gas is unphysical (m^3 < 0).")
    return (number_of_moles * R * temperature) / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines the allowed transistions between 2 quantum states
    
    Args:
        v_0 (int): the original vibrational energy level
        v_1 (int): the final vibrational energy level
    
    Returns:
        Boolean: if the transistion is allowed
    """
    if v_0 < 0:
        raise ValueError("The energy level must be greater than or equal to 0.")
    if v_1 < 0:
        raise ValueError("The energy level must be greater than or equal to 0.")   
    if not isinstance(v_0, int):
        raise TypeError("The vibrational energy level must be an integer.")
    if not isinstance(v_1, int):
        raise TypeError("The vibrational energy level must be an integer.")
    
    difference = v_1 - v_0
    if difference == (-1):
        return True
    elif difference == 1:
        return True
    else: 
        return False
  
     

# Function for coulomb
from scipy.constants import epsilon_0, pi

def coulomb(r, q_i, q_j):
    """
    Determines the potential energy between two charged particles
    
    Args:
        r (array_like, int): the seperation of two charged particles
        q_i (int): charge of molecule i
        q_j (int): charge of molecule j
    
    Returns:
        array_like, float: the potential energy between i and j
    """
    
    return np.array(q_i * q_j) / (pi* epsilon_0 * np.array(r) * 4)
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the goodness of fit of experimental data to a model 
    
    Args:
        model (array_like, float): the model of data
        exp (array_like, float): the experimental data
        ex_uncertainity (array_like, float): the experimental uncertainity
    
    Returns:
        the goodness of fit of the model
    """
    if len(model) == len(exp) == len(exp_uncertainty):
        return np.sum(((exp - model) / exp_uncertainty)**2)
    else:
        raise ValueError("lengths of values are not the same length")
    


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution to the partition function
    
    Args:
        N (int): the max energy level
        rotational_constant (float): the rotational constant for the molecule (cm-1)
        temperature (float): the temperature (K)
    
    Returns:
        float: the rotational contribution to the partition function
    """
    if not isinstance(N, int):
        raise TypeError("The energy level must be an integer.")
    if rotational_constant < 0:
        raise ValueError("The rotational constant must be greater than or equal to 0.") 
    if temperature < 0:
        raise ValueError("The temperature cannot be unphysical (T < 0K).") 
    
    total = 0 #create an empty variable to add to
    numbers = list(range(0, N + 1)) #create a list of N values
    for n in numbers:
        q = ((2.0 * n) + 1.0) * np.exp((- h * c * (rotational_constant*100) * n * (n + 1.0))/(k * temperature))
        total = total + q #adding to total (same as sum equation)
    return total
                                     












