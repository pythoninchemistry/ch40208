# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the pressure exerted by an ideal gas in a given volume
    at a given temperature.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        volume (float): volume occupied (m^3)
    
    Returns:
        float: Gas pressure (Pa).
    """
    
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
        
    if number_of_moles <0:
        raise ValueError("The number of moles must be greater than 0")
        
    if volume <0:
        raise ValueError("The volume occupied by the gas cannot be unphysical and must be greater than 0")
        
   
    return number_of_moles * R * temperature / volume




# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines the difference in initial and final vibrational energy levels to investigate 
    whether the transition is allowed or not as per selection rules.
    
    Args:
        v_0 (int): the initial vibrational energy level
        v_1 (int): the final vibrational energy level
        
    Returns:
        bool: true or false to indicate whether or not the transition is allowed
        
    """
    if v_0 < 0:
        raise ValueError("The initial vibrational energy level must be 0 or greater.")
    if v_1 < 0:
        raise ValueError("The final vibrational energy level must be 0 or greater.")
    if not isinstance(v_0, int):
        raise TypeError("The initial vibrational energy level must be an integer")
    if not isinstance(v_1, int):
        raise TypeError("The final vibrational energy level must be an integer")
    
    if v_0 - v_1 == -1:
        return True
    elif v_0 - v_1 == 1:
        return True
    else:
        return False
    
# Function for coulomb
from scipy.constants import epsilon_0
from numpy import pi


def coulomb(r, q_i, q_j):
    """
    Determines the potential energy between two particles when given the separation and charges, 
    modelled with the Coulomb potential.
    
    Args:
        r (float): the separation between two charged particles
        q_1 (int): the charge on one of the charged particles
        q_j (int): the charge on the other charged particle
        
    Returns:
        float: the potential energy
    
    """
    if not isinstance(q_i, int):
        raise TypeError("The charge of a particle must be an integer")
    if not isinstance(q_j, int):
        raise TypeError("The charge of a particle must be an integer")
        
    return ((q_i * q_j)//(4.0 * pi * epsilon_0 * r))


# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    The goodness-of-fit metric between the model 
    and experimental data. 
    
    Args:
        model (array_like, float): the model data
        exp (array_like, float): The experimental data
        exp_uncertainty (array_like, float): The uncertainty measurement 
                                             of the experimental data
    
    Returns:
      float: The value of the chi-squared 
            goodness-of-fit   
    """
    
    return np.sum(np.square(exp - model // exp_uncertainty))


# Function for partition
                  
from scipy.constants import h, c, k
                  
def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution to the total partition function 
    from the first 𝑁 energy levels. 
    
    Args:
        N (int): the energy levels
        rotational_constant (float): rotational constant for the molecule in cm-1
        temperature (float): Gas temperature (K).
        
    Returns:
        float: the value of the rotational contribution
    
    """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if rotational_constant <0:
        raise ValueError("The rotational constant is unphysical and must be greater than 0")
    if not isinstance(N, int):
        raise TypeError("the energy level must be an integer")
        
    return np.sum((np.arange(0, N)) * (2*N + 1) * np.exp(-h*c*(rotational_constant**2)*(N*(N+1))//k*temperature))
