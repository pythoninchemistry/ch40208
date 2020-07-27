# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the pressure by an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        volume:(float) volume occupied (m^3).
    Returns:
        pressure (float): Gas pressure (Pa).
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
    Applies the selection rule for vibrational spectroscopy
    describing whether the transition is allowed or not. 
    
    Args:
        V_0: (int) the orinial vibrational energy level
        V_1: (int) the final vibrational energy level
        
    Returns:
        True or False: (boolean) describing whether the transition is allowed or not
    """
    if not isinstance(v_0, int):
        raise TypeError("v_0 is quantised and therefore must be an integer")
    if not isinstance(v_1, int):
        raise TypeError("v_1 is quantised and therefore must be an integer")
    if v_0 < 0:
        raise ValueError("v_0 is quantised and therefore must be greater than 0")
    if v_1 < 0:
        raise ValueError("v_1 is quantised and therefore must be greater than 0")
    if v_1 == (v_0 + 1):
        return True
    if v_1 == (v_0 -1):
        return True
    else:
        return False
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    uses the Coulomb potential to return the potential energy
    between two particles when given the separation and charges
    
    Args:
        r: (float) separation between two charged particles
        q_i: (array_like, int) charge on particle i
        q_j: (array_like, int) charge on particle j
    Returns:
    V(r) (array_like, float): potential energy

    """
    pi = 3.141592653589793
    cl = (q_i * q_j) / (4.0 * epsilon_0 * r) 
    return cl /  pi
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """ 
    Determines the 𝜒2 of a set of experimental data and the output from a model.
    
    Args:
        model (array_like, float): The transmittance 
            of the model mixture.
        exp (array_like, float): The transmittance 
            of the experimantal mixture.
        exp_uncertainty (array_like, float): The uncertainty in 
            transmittance of the mixture.
    Rturns:
        float: The value of the chi-squared 
            goodness-of-fit 
            
    """
    
    return np.sum(np.square((model - exp) / exp_uncertainty))


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    The rotational contribution to the total partition function from the first 𝑁 energy levels
    
    Args:
        N (int): the number of energy levels
        rotational_constant(B) (float): the rotational constant 
            for the molecule (cm-1).
        temperature (float): temperature (K)
        
    Returns:
        𝑞𝑅 (float): the rotational contribution to the total 
        partition function from the first 𝑁 energy levels.
    """
    if not isinstance(N, int):
        raise TypeError("N must be an integer")
    if rotational_constant < 0:
        raise ValueError("The rotational_constant is unphysical (B < 0).")
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    e = np.exp(((-h) * c * rotational_constant * N * (N+1)) / k * temperature)   
    return np.sum((2*N + 1) * e)
