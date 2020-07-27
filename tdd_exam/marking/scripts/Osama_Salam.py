# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates using the ideal gas law
    
    Args:
        number_of_moles(int): the number of moles of gas in the system
        temperature(float): temperature of system in kelvin
        volume(float): volume of system in metres cubed
        
    Returns:
        float: pressure of system in pascals
    """
    if number_of_moles < 0:
        raise ValueError("Number of moles given is unphysical (n < 0)")
    
    if temperature < 0:
        raise ValueError("Temperature given is unphysical (T < 0)")
   
    if volume < 0:
        raise ValueError("Volume given is unphysical (V < 0)")
    
    pressure = (R * number_of_moles * temperature) / volume

    return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether a transition between vibrational quantum states is allowed or not
    
    Args:
        v_0(int): initial vibrational energy level
        v_1(int): final vibrational energy level
    
    Returns:
        bool: True for allowed transition, False for disallowed transition
    """
    
    if not isinstance (v_0, int):
        raise TypeError("Initial vibrational energy level must be an integer")
     
    if not isinstance (v_1, int):
        raise TypeError("Final vibrational energy level must be an integer")
        
    if v_0 < 0:
        raise ValueError("Initial vibrational energy level must be greater than or equal to zero")
        
    if v_1 < 0:
        raise ValueError("Final vibrational energy level must be greater than or equal to zero")
    
    delta_v = v_1 - v_0
    
    if delta_v == 1 or delta_v == -1:
        answer = True
        
    else:
        answer = False
    
    return answer
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Calculates potential energy between two particles from the separation and charges
    
    Args:
        r(array_like, int): separation between particles
        q_i(int): charge on particle i
        q_j(int): charge on particle j
        
    Returns:
        array_like, float: Potential energy between particles
    """
    
    
    if type(r) == int:
        V_r = (q_i * q_j) / (4 * np.pi * epsilon_0 * r)
    
    elif type(r) == list:
        for i in range(0, len(r)):
            V_r = np.array((q_i * q_j) / (4 * np.pi * epsilon_0 * np.array(r))) 
    
    return V_r
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculates goodness-of-fit chi squared of experimental data from its uncertainties and model data
    
    Args:
        model(array_like, float): model data
        exp(array_like, float): experimental data
        exp_uncertainty(array_like, float): uncertainties in experimental data
        
    Returns:
        float: chi squared value for experimental data
    """
    
    if len(exp) < len(model):
        raise ValueError("Experimental data has too few values")
    
    if len(model) < len(exp):
        raise ValueError("Model data has too few values")
    
    if len(exp_uncertainty) < len(exp):
        raise ValueError("Uncertainties for experimental data has too few values")
    
    chi_squared = np.sum((((exp - model) / exp_uncertainty)**2))
    
    return chi_squared


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates rotational contribution to partition function
    
    Args:
        N(int): number of energy levels
        rotational_constant(float): rotational constant for the molecule
        temperature(float): temperature
        
    Returns:
        float: rotational contribution to partition function, q_R
    """
    if not isinstance (N, int):
        raise TypeError("N must be an integer")
    
    if rotational_constant < 0:
        raise ValueError("Rotational constant given is unphysical (B < 0)")
                        
    if temperature < 0:
        raise ValueError("Temperature given is unphysical (T < 0)")
                        
    J = np.linspace(0, N + 1, N + 1, False)
    
    for i in range(0, len(J)):
        q_R = np.sum(((2 * J[i]) + 1) * np.exp((-h * c * rotational_constant * J[i] * (J[i] + 1)) / (k * temperature)))

    return q_R

