# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the volume occupied by an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        volume (float): Volume occupied (m^3).
    
    Returns:
        float: Gas pressure (Pa)
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
    Determine whether a transition is allowed or not in vibrational spectroscopy
    
    Args: 
       v_0 (int): Initial vibrational energy level
       v_1 (int): Final vibrational energy level
    
    Returns:
        bool: Allowed transitions
    """
    if v_0 < 0:
        raise ValueError("The initial vibrational energy level must be greater than or equal to 0.")
    if v_1 < 0:
        raise ValueError("The final vibrational energy level must be greater than or equal to 0.")    
    if not isinstance(v_0, int):
        raise TypeError("The initial vibrational energy level must be an integer")
    if not isinstance(v_1, int):
        raise TypeError("The final vibrational energy level must be an integer")
    if v_0 == v_1 + 1:
        return True
    if v_0 == v_1 -1:
        return True
    else:
        return False
     

# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    """
    Determines the energy potential between 2 particles
    
    Args: 
       r (array_like, float): Separation between 2 particles (Å)
       q_i (float): Charge on particle i
       q_j (float): Charge on particle i
    
    Returns:
        array_like, float: Potential energy, V(r), in Jmol^-1
    """
    if isinstance(R, int):
        return (q_i*q_j)/(4*pi*epsilon_0*r)
    if isinstance(R, float):
        return np.arange((q_i*q_j)/(4*pi*epsilon_0*r))
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines chi_squared for a set of experimental data and the output from a model
    
    Args: 
       model (float): Model data
       exp (array_like): Experimental data
       exp_uncertainty (array_like): Experimental uncertainty in the measurement of exp
    
    Returns:
        array_like: Chi_squared, the goodness of fit
    """
    return np.sum(np.square((model - exp) / exp_uncertainty))
#if arrays not same length:
    #raise IndexError("tuple index out of range")

# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution to the total partition function
    
    Args: 
       N (int): The number of energy levels
       rotational_constant (float): Rotational constant of molecule (cm^-1)
       temperature (float): Temperature (K)
    
    Returns:
        float: The rotational contribution
    """
    J=np.arange(0,N+1)
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if rotational_constant < 0:
        raise ValueError("The rotational constant is unphysical (rotational_constant < 0).")
    if not isinstance(N, int):
        raise TypeError("N must be an integer")   
    return np.sum((2*J+1)*np.exp((-h*c*rotational_constant*100*J*(J+1))/(k*temperature)))
