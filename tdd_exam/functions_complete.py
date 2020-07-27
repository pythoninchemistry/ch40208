# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, pressure):
    """
    Determine the pressure of an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        volume (float): Gas pressure (Pa).
    
    Returns:
        float: Volume occupied by gas (m^3).
    """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if number_of_moles < 0:
        raise ValueError("The number of moles is unphysical (n < 0).")
    if pressure < 0:
        raise ValueError("The pressure is unphysical (p < 0).")
    return number_of_moles * R * temperature / pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Evaluates if a given vibrational energy level change is allowed 
    by the vibrational spectroscopic selection rules.
    
    Args:
        v_0 (int): The initial vibrational energy level.
        v_1 (int): The final vibrational energy level. 
        
    Returns:
        bool: If the transition is allowed. 
    """
    if (v_0 < 0 or v_1 < 0):
        raise ValueError("One or both of the vibrational energy "
                         "levels is/are less than 0")
    if not (isinstance(v_0, int) and isinstance(v_1, int)):
        raise TypeError("One or both of the vibrational energy "
                        "levels is/are not integer values")
    if np.abs(v_0 - v_1) == 1:
        return True
    else:
        return False
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Find the potential energy between to particles as a 
    result of the Coulombic interaction. 
    
    Args: 
        r (array_like, float): The separation value(s)
        q_i (float): The charge on atom i
        q_j (float): The charge on atom j
    
    Returns:
        array_like, float: The potential energy value(s)
    """
    r = np.array(r)
    return q_i * q_j / (4 * np.pi * epsilon_0 * r)
        
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Find the chi-squared value between a model and some 
    experimental data with a given uncertainty. 
    
    Args:
        model (array_like, float): The model data
        exp (array_like, float): The experimental data
        exp_uncertainty (array_like, float): The 
            experimental uncertainty data
    
    Returns:
        float: The chi-squared goodness-of-fit value
    """
    if len(exp) != len(model) or len(model) != len(
        exp_uncertainty) or len(exp_uncertainty) != len(
        exp):
            raise ValueError("The length of the model, exp, and "
                             "exp_uncertainty arrays are not all "
                             "the same")
    return np.sum(np.square((exp - model) / exp_uncertainty))


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determine the rotational contribution to the 
    partition function.
    
    Args:
        N (int): Number of energy levels to consider.
        rotational_constant (float): Molecular rotational
            constant (cm^-1).
        temerature (float): System temperature (K).
    
    Returns:
        float: Rotational contribution to partition function.
    """
    if rotational_constant < 0:
        raise ValueError("The rotational constant must be "
                         "greater than 0.")
    if temperature < 0:
        raise ValueError("The temperature must be greater than 0.")
    if not isinstance(N, int):
        raise TypeError("The number of energy levels to consider "
                        "must be an integer.")
    qR = 0
    for j in range(0, N+1):
      degeneracy = (2 * j + 1)
      energy = rotational_constant * h * c * 1e2 * j * ( j + 1 )
      qR += degeneracy * np.exp( - energy / (k * temperature) )
    return qR