# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Uses a rearranged form of the ideal gas law to solve for 
    the pressure of asystem
    
    Args:
        number_of_moles (float): number of moles in the system (mol)
        temperature (float): temperature of the system (K)
        volume (float): total volume of the system (m^3)
        
    Returns:
        Float: The pressure of the system (Pa)
    
    """
    # Raising error if T < 0
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
        
    # Raising error if no. moles < 0
    elif number_of_moles < 0:
        raise ValueError("The number of moles is unphysical (n < 0).")
    
    # Raising error if volume < 0
    elif volume < 0:
        raise ValueError("The volume is unphysical (n < 0).")
        
    # Performing calculation of pressure if all conditions are met
    else:
        p = (number_of_moles * R * temperature) / volume
    
    return p




# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determining if the transition between two vibrational levels is
    allowed based of the vibrational spectroscopy selection rules which
    are del_nu = +/- 1
    
    Args:
        v_0 (int): the original vibrational energy level
        v_1 (int): the new/final vibrational energy level
        
    Returns:
        int: the delta v of the original and final vibrational energy levels
    """
    
    del_v = v_1 - v_0
    
    # Testing negative values for v_0 and v_1
    if v_0 < 0 or v_1 < 0:
        raise ValueError('The value for v_0 and v_1 must be 0 or greater')
        
    # Testing for v_0 and v_1 being an integer
    elif not isinstance(v_0, int):
        raise TypeError("v_0 must be an integer")
    elif not isinstance(v_1, int):
        raise TypeError("v_1 must be an integer")
        
    # Testing selection rule
    elif del_v == 1 or del_v == -1:
        return True
    elif del_v != 1 or del_v != -1:
        return False
    
    
    
    
# Function for coulomb
from scipy.constants import epsilon_0
from math import pi

def coulomb(r, q_i, q_j):
    """
    Determines the potential energy between two charges when the separation
    between them is known. Modelled using the Coulomb potential
    
    Args:
        r (list_like, float): separation between the charged particles i and j (some unit of length)
        q_i (float): charge on atom i (C)
        q_j (float): charge on atom j (C)
    
    Returns:
        float: The potential energy (C)
    """
    V = (q_i * q_j) / (4 * pi * epsilon_0 * r)
    
    return V




# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Evaluating the goodness-of-fit, chi squared, for which a lower value is
    more desirable
    
    Args:
        model (array): model data points
        exp (array): experimental data points
        exp_uncertainty (array): uncertainty in said experimental data points
        
    Returns:
        Float: Chi_squared which is a measure of goodness-of-fit for the experimental data
    """
    # Testing for an error raise when the length of each array is different
    if len(model) != len(exp) != len(exp_uncertainty):
        raise ValueError('Each component of the array must possess the same number of items')
    
    # Peforming calculation of chi squared if all conditions are met
    else:
        chi_sq = np.sum(((exp - model) / exp_uncertainty) ** 2)
    
    return chi_sq




# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates the rotational contribution to the partition function when the number
    of energy levels, rotational constant and temperature of the system are known
    
    Args:
       N (int): number of rotational energy levels being considered
       rotational_constant (float): a constant relating to the energy spacing between levels? (cm-1)
       temperature (float): temperature of the system (K)
   
   Returns:
       float: the rotational partition funcition of the molecule 
    """
    B = rotational_constant
    T = temperature
    
    # Creating a list of possible values for N, called energy_levels
    energy_levels = np.arange(0, N + 1)
    
    # Creating an empty value for total partition function to add the values onto
    total_q = 0
    
    # Raising error when T < 0
    if T < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
        
    # Raising error when B < 0
    elif B < 0:
        raise ValueError("The rotational constant is unphysical (T < 0).")
    
    # Raising error for when N is not an integer
    elif not isinstance(N, int):
        raise TypeError("N must be an integer")
    
    # Performing the calculation if all conditions are met
    # Converting B into m-1 so that units cancel
    # Adding each calculation onto that of the previous energy level
    for J in energy_levels:
        q_r = ((2 * J) + 1) * np.exp((-h * c * (B * 1e2) * J * (J + 1)) / (k * T))
        total_q += q_r
    
    return total_q




