# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """"
    This calculates the volume of an ideal gas.
    
    Args:
        number_of_moles (float): The number of moles of the ideal gas.
        temperature (float): The temperature of the ideal gas (K).
        volume (float): The volume of the ideal gas (m^3).
        
    Returns:
        float: The pressure of the ideal gas (Pa).
    """
    if number_of_moles < 0:
        raise ValueError("The number of moles given is unphysical (n < 0).")
    if temperature < 0:
        raise ValueError("The temperature given is unphysical (T < 0 K).")
    if volume < 0:
        raise ValueError("The volume given is unphysical (V < 0 Pa).")
    return (number_of_moles * R * temperature) / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    This determined whether transition between the given vibrational energy levels is allowed.
    
    Args:
        v_0 (int): The initial vibrational energy level.
        v_1 (int): The final vibrational energy level.
        
    Returns:
        Boolean: Determines whether given transition is allowed (True) or not allowed (False).
    """
    if not isinstance(v_0, int):
        raise TypeError("v_0 must be an integer.")
    if not isinstance(v_1, int):
        raise TypeError("v_1 must be an integer.")
    if v_0 < 0:
        raise ValueError("v_0 must be greater than 0.")
    if v_1 < 0:
        raise ValueError("v_1 must be greater than 0.")
    if (v_0 - v_1) == 1 or (v_0 - v_1) == -1:
        return True
    else:
        return False
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    This calculates the potential energy between two charge particles.
    
    Args:
        r (list_type, float): The separation between the two particles (m).
        q_i (int): The relative charge of particle i.
        q_j (int): The relative charge of particle j.
    
    Return:
        float: The potential energy between particles i and j.
    """
    R = np.array(r)
    answer = (q_i * q_j) / (4 * np.pi * epsilon_0 * R)
    return answer    
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    This determines the chi squared value for a given set of data and a model.
    
    Args:
        model (array_like, float): The model data set.
        exp (array_like, float): The experimental data set.
        exp_uncertainty (array_like, float): The uncertainty values on the experimental data set.
    
    Returns:
        float: The chi squared values for the experimental data and the model.
    """
    if len(model) == len(exp) and len(model) == len(exp_uncertainty):
        return np.sum(((exp - model) / exp_uncertainty) **2)
    if len(model) < len(exp) and len(model) < len(exp_uncertainty):
        raise ValueError("There are too few data points in the model data set.")
    if len(model) > len(exp) and len(model) > len(exp_uncertainty):
        raise ValueError("There are too many data points in the model data set.")
    if len(exp) < len(model) and len(exp) < len(exp_uncertainty):
        raise ValueError("There are too few data points in the experimental data set.")
    if len(exp) > len(model) and len(exp) > len(exp_uncertainty):
        raise ValueError("There are too many data points in the experimental data set.")
    if len(exp_uncertainty) < len(model) and len(exp_uncertainty) < len(exp):
        raise ValueError("There are too few data points in the experiment uncertainty data set.")
    if len(exp_uncertainty) > len(model) and len(exp_uncertainty) > len(exp):
        raise ValueError("There are too many data points in the experiment uncertainty data set.")
    if len(model) != len(exp) and len(model) != len(exp_uncertainty):
        raise ValueError("The number of data points is different in all three data sets.")
        
        
# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    This calculates the rotational contribution to the molecular partition function.
    
    Args:
        N (int): The number of rotational energy levels.
        rotational_constant (float): The rotational constant for the molecule (cm^-1).
        temperture (float): The temperature at which the partition function is calculated (K).
    """
    if not isinstance(N, int):
        raise TypeError("N must be an integer.")
    if rotational_constant < 0:
        raise ValueError("The rotational constant given is unphysical (B < 0 cm^-1)")
    if temperature < 0:
        raise ValueError("The temperature given is unphysical (T < 0 K)")    
    J = np.arange(N + 1)
    total = ((2 * J) + 1) * np.exp(-((h * c * rotational_constant * J * (J + 1)) / k * temperature))
    return np.sum(total)