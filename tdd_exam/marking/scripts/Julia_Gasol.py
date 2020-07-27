# Import numpy
import numpy as np
import math

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the pressure of an ideal gas
    
    Args:
        number_of_moles (float): Number of moles of ideal gas (mol)
        temperature (float): Gas temperature (K)
        volume (float): Volume occupied by the gas (m^3)
        
    Returns:
        float: gas pressure (Pa)
    """
    if temperature < 0:
        raise ValueError('The temperature is unphysical T < 0 K.')
    if number_of_moles < 0:
        raise ValueError('The number of moles of gas is unphysical n < 0 mol.')
    if volume < 0:
        raise ValueError('The volume of gas is unphysical V < 0 m^3.')
    return number_of_moles * R * temperature / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determine if a tranistion is allowed or not
    
    Args:
       v_0 (int): Original vibrational energy level
       v_1 (int): Final vibrational energy level 
       
    Returns:
        Whether the transition is allowed or not
    """        
    if v_0 <= 0:
        raise ValueError('The vibrational energy level must be greater than 0.')
    if v_1 <= 0:
        raise ValueError('The vibrational energy level must be greater than 0.')
    if not isinstance(v_0, int):
        raise TypeError('The vibrational energy level must be an integer.')
    if not isinstance(v_1, int):
        raise TypeError('The vibrational energy level must be an integer.')

    
    elif (v_1 - v_0) < - 1 and (v_1 - v_0) > 1:
        print (False)
    else:
        print (True)
    return print()

  

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Determine the potential energy between two charged particles using the Coulomb potential.
    
    Args:
        r (array_like, float): Separation between the charged particles (Angstrom).
        q_i (int): Charge of particle 1.
        q_j (int): Charge of partice 2.
        
    Return:
        array_like, float: Potential energy (eV).
    """
    if not isinstance(q_i, int):
        raise TypeError('The particle charge must be an integer.')
    if not isinstance(q_j, int):
        raise TypeError('The particle charge must be an integer.')
    return (q_i * q_j / 4.0 * np.pi * epsilon_0 * r) * (10 ** 18)

# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    The goodness-to-fit metric (i.e. chi squared value) between the model and the experimental data.
    
    Args:
        model (array_like, float): The model function.
        exp (array_like, float): The summation over all data points.
        exp_uncertainty (array_like, float): The experimental uncertainty in the measurement of exp.
        
    Returns:
        float: The value of chi squared, goodness-to-fit.
    """
    goodness_of_fit = np.sum(np.square((model - exp) / exp_uncertainty))
    return goodness_of_fit
    

# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculte the rotational contribution to a molecular partition.
    
    Args:
        N (int): Number of energy levels.
        rotational_constant (float): Rotational contant for the molecule, B (cm^-1).
        temperature (float): temperature of the system (K).
        
    Return:
       float: The rotational contribution.
    """
    if temperature < 0:
        raise ValueError('The temperature is unphysical T < 0 K.')
    if rotational_constant < 0:
        raise ValueError('The rotational constant is unphysical n < 0 cm^-1.')
    if not isinstance(N, int):
        raise TypeError('The number of energy levels must be an integer.')
    part = np.sum((2 * np.arange(0, N+1) + 1) * 
                 np.exp(-h * c * (1 / rotational_constant * (10 ** -2)) * 
                        np.arange(0, N+1) * (np.arange(0, N+1) + 1) / k * temperature)) 
    return part