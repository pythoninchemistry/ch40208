# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """Determine the pressure of an an ideal gas
    
    Args:
        number_of_moles (float): Number of moles of ideal gas
        temperature (float): Gas Temperature (K)
        volume (float): Volume occupied by ideal gas (m^3)
      
        
    Returns:
        float: pressure of ideal gas (Pa)
    """
    if temperature < 0:
        raise ValueError("The Temperature is unphysical (T < 0).")
    if volume < 0:
        raise ValueError("The volume is unphysical (V < 0).")
    if number_of_moles < 0:
        raise ValueError("The number of moles is unphysical (n < 0).")
    return (number_of_moles * R * temperature) / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """Will give a boolean variable to describe whether a transition is allowed
       or not given quantised vibrational energy levels
       
    Args: 
        v_0 (int): intial vibrational energy level
        v_1 (int): final vibrational energy level
        
    Returns:
        (bool): whether transition is allowed or not (True = Allowed, False = Forbidden)
    """
    x = v_0 + 1
    y = v_0 - 1
     
    
    if v_1 < 0:
        raise ValueError("v_1 cannot be negative")
    if v_0 < 0:
        raise ValueError("v_0 cannot be negative")
    if v_0 and v_1 < 0:
        raise ValueError("v_0 and v_1 cannot be negative")
    if v_1 == x:
        return True
    if v_1 == y:
        return True
    else:
        return False
    
     

# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    """Will return the potential energy between two particles given the charges and separation
    
    Args:
        r (array_like, float): distance between particles
        q_i (float): charge of particle i
        q_j (float): charge of particle j
        
    Returns:
        array_like, float: Potential energy between the two particles
    """
   
    return (q_i * q_j)/(4 * pi * epsilon_0 * r)
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """Provides a  goodness-of-fit metric (chi squared) between a model 
    and experimental data.
    
    Args:
        model (float):y values of model data
        exp (float): y values of experimental data
        exp_uncertainty (float): error associated with experimental y values
        
    Returns: 
        float: The value of chi squared
    """
    chi = np.sum(np.square((
        model - exp) / exp_uncertainty))
    return chi


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """Will return the rotational partition function given the number of energy levels,
       the rotational constant and the temperature
       
    Args:
        N (int): number of energy levels
        rotational_constant (float): rotational constant of the molecule (cm^-1)
        temperature (float): temperature (K)
        
    Returns:
        float: the rotational partition function
    """
    J_values = [0,N,1]
    if rotational_constant < 0:
        raise ValueError("Rotational Constant cannot be negative")
    if temperature < 0:
        raise ValueError("Temperature cannot be negative")
    
 
    return np.sum(((2 * J_values) + 1) * np.exp((-h * c * rotational_constant * J_values * (J_values + 1))/(k * temperature)))
    
    
    
    