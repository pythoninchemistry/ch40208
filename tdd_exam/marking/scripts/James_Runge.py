# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the pressure of an ideal gas from the 
    number of moles of gas, the temperature and the volume of
    gas
    
    Args: 
         number_of_moles (float): The number of moles of gas
         temperature (float): The temperature of the gas (K)
         volume (float): The volume of gas (m^3)
         
    Returns: 
         float: The pressure of the gas (Pa)
    """
    if temperature < 0:
        raise ValueError("The temperature of the gas is unphysical (T < 0)")
    if number_of_moles < 0:
        raise ValueError("The number of moles is unphysical")
    if volume < 0:
        raise ValueError("The volume of gas is unphysical (V < 0)")
    else:
        return number_of_moles * R * temperature / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Describes whether a transition between one quantum
    state and another is allowed or not
    
    Args:
         v_0 (int:) The inital energy level of the quantum
                    state
         v_1 (int:) The final energy level of the quantum
                    state
    
    Returns:
         bool: True or False statement describing whether a
               transition is allowed or not
    """
    if v_1 <=0:
        raise ValueError("Vibrational energy levels are quantised (must be greater than 0)")
    if v_0 <=0:
        raise ValueError("Vibrational energy levels are quantised (must be greater than 0)")
    if v_1 <=0 and v_0 <=0:
        raise ValueError("Vibrational energy levels are quantised (must be greater than 0)")
    if not isinstance(v_1, int):
        raise TypeError("Vibrational energy levels are quantised (value must be an integer)") 
    if not isinstance(v_0, int):
        raise TypeError("Vibrational energy levels are quantised (value must be an integer)")  
    if not isinstance(v_1, int) and not isinstance(v_0, int):
        raise TypeError("Vibrational energy levels are quantised (value must be an integer)") 
   
    return v_1 -+ v_0 == 1
    v_0 - v_1 ==1
    v_1 + v_0 != 1
    v_1 - v_0 != 1
    

        
# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Determines the potential energy of two particles when given
    the separation and charges
    
    Args:
        r (float): The separation between two molecules
        q_i (int): The charge of lithium, 1
        q_j (int): The charge of oxygen, -2
        
    Returns:
         array-like, float: The charge separation between two molecules
    """
    import numpy as np
    return (q_i*q_j) / (4 * np.pi * epsilon_0 * r)
           
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the chi-squared of an experimental
    data set and the output of a model
    
    Args:
        model (array-like, float): The model data set
        exp (array-like, float): The experimental data set
        exp_uncertainty (array-like, float): The uncertainty in the experimental data
        
    Returns:
        float: The chi-squared value for the experimental data
    """
    chi = np.sum(np.square((exp - model) / exp_uncertainty))
    return chi
    


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution from the first N
    energy levels
    
    Args:
        N (int): The number of energy levels
        rotational_constant (float): The rotation constant of the molecule (cm^-1)
        temperature (float): The temperature (K)
        
    Returns:
         array-like, float: the rotational contribution to the partition constant
    """
    rot_contribution = np.sum((2* N + 1)*np.exp((-h*c*rotational_constant*N*(N+1)) / k * temperature))
    return rot_contribution