# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determines the pressure occupied by an ideal gas.
    
    Args:
        number_of_moles (float): The number of moles of gas.
        temperature (float): The temperature of the gas (K).
        volume (float): The volume occupied by the gas (m^3).
    
    Returns:
        float: The pressure of the gas (Pa).
    """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if number_of_moles < 0:
        raise ValueError("The number of moles is unphysical (n < 0).")
    if volume < 0:
        raise ValueError("The volume is unphysical (V < 0).")
    return number_of_moles * R * temperature / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines if the transition between two vibrational energy levels is allowed.
    
    Args:
        v_0 (int): The original vibrational energy level.
        v_1 (int): The final vibrational energy level.
        
    Returns:
        bool: True if allowed, False if not allowed.
    """
    if not isinstance(v_0, int):
        raise TypeError("v_0 must be an integer.")
    if not isinstance(v_1, int):
        raise TypeError("v_1 must be an integer.")
    if v_1 - v_0 == 1:
        return True
    if v_1 - v_0 == -1:
        return True
    if v_0 < 0:
        raise ValueError("v_0 must be positive.")
    if v_1 < 0:
        raise ValueError("v_1 must be positive.")
    else:
        return False
   
        
# Function for coulomb
from scipy.constants import epsilon_0
from math import pi

def coulomb(r, q_i, q_j):
    """
    Determines the potential energy between two charged particles.
    
    Args:
        r (array_like, float): The seperation of the particles.
        q_i (int): The charge of the first particle.
        q_j (int): The charge of the second particle.
    
    Returns:
        float: The potential energy.
    """
    for i in np.array([r]):
        result = (q_i * q_j) / (4 * pi * epsilon_0 * i)
    return result

    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the goodness-of-fit parameter for a set of experimental data
    
    Args:
        model (array_like, float): The model. 
        exp (array_like, float): The experimental data.
        exp_uncertainty (array_like, float): The experimental uncertainty of exp
    
    Returns:
        float: goodness_of_fit
    """
    if len(exp) != 3:
        raise ValueError("The experimental data has too few values.")
    if len(model) != 3:
        raise ValueError("The model has too few values.")
    if len(exp_uncertainty) != 3:
        raise ValueError("The experimental uncertainty of exp has too few values.")
    for d in np.array([exp]):
        for e in np.array([model]):
            for f in np.array([exp_uncertainty]):
                return np.sum(((d - e)/f)**2)


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution to the molecular partition function.
    
    Args:
        N (int): 
        rotational_constant (float): The rotational constant for the molecule (cm-1).
        temperature (float): The temperature (K).
    
    Returns:
        float: The rotational contribution.        
    """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if rotational_constant < 0:
        raise ValueError("The rotational constant is unphysical (B < 0).")
    if not isinstance(N, int):
        raise TypeError("N must be an integer.")
    for n in range(0, N+1):
        return np.sum((2*n + 1) * np.exp(-h * c * rotational_constant * 100 * n*(n+1)
                       / k*temperature)