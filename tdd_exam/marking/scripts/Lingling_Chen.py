# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculate the pressure of an ideal gas
    
    Args:
        number_of_moles (float): number of moles of ideal gas.
        temperature (float): temperature of gas (K).
        volume (float): volume of gas (m^3).
        
    Returns:
        float: pressure of gas (Pa).
    """
    if number_of_moles < 0:
        raise ValueError('the number of moles of gas '
                         'cannot be less than 0')
    if temperature < 0:
        raise ValueError('the temperature value in Kelvin'
                         'cannot be less than 0')
    if volume < 0:
        raise ValueError('the volume value in m^3'
                         'cannot be less than 0')
    return (number_of_moles * R * temperature) / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether the vibrational transition
    is allowed 
    
    Args:
        v_0 (integer): the original vibrational energy level.
        v_1 (integer): the final vibrational energy level.
        
    Returns:
        Boolean: allowed transition or not.
    """
    if not isinstance(v_0, int):
        raise TypeError('the original vibrational energy level (v) '
                        'must be an interger')
    if v_0 < 0:
        raise ValueError('the original vibrational energy level (v) '
                         'value must be greater than 0')
    if not isinstance(v_1, int):
        raise TypeError('the final vibrational energy level (v) '
                        'must be an interger')
    if v_1 < 0:
        raise ValueError('the final vibrational energy level (v) '
                         'value must be greater than 0')
    return ((v_1 - v_0) >= -1 
            and (v_1 - v_0) <= 1)
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Calculate the potential energy between 
    two charged particles
    
    Args:
        r (float): distance between particles.
        q_i (integer): the charge on one particle.
        q_j (integer): the charge on the other particle.
        
    Returns:
        float: potential energy.
    """
    potential_energy = []
    if isinstance(r, int):
        potential_energy = (q_i * q_j) / (4 * np.pi * epsilon_0 * r)
           
    elif isinstance(r, list):
        for i in range(0,len(r)):
            values_potential_energy = (q_i * q_j) / (4 * np.pi * epsilon_0 * r[i])
            potential_energy.append(values_potential_energy)
        
    return potential_energy
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculate the goodness-of-fit between the experimental data and model
    
    Args:
        model (float): data of the model.
        exp (float): data of the experimental measurements.
        exp_uncertainty (float): uncertainty in the measurements.
    
    Returns:
        float: chi-squared value        
    """
    if len(model) == len(exp) and len(exp) != len(exp_uncertainty):
        raise ValueError('the uncertainty of experimental data '
                     'has different amount of values than others')
    if len(model) == len(exp_uncertainty) and len(exp_uncertainty) != len(exp):
        raise ValueError('the experimental data '
                     'has different amount of values than others')
    if len(exp) == len(exp_uncertainty) and len(exp_uncertainty) != len(model):
        raise ValueError('the model '
                     'has different amount of values than others')
    chi_squared = np.sum(np.square((model - exp) / exp_uncertainty))
    return chi_squared


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculate the rotational contribution to the total 
    partition function from the first N energy levels
    
    Args:
        N (integer): the number of energy levels
        rotational_constant (float): rotational constant for the molecule
        temperature (int): the temperature (K)
        
    Returns:
        float: rotational contribution
    """
    if not isinstance(N, int):
        raise TypeError('number of energy levels '
                    'must be an interger')
    if rotational_constant < 0:
        raise ValueError('the rotational_constant '
                     'cannot be less than 0')
    if temperature < 0:
        raise ValueError('the temperature value '
                     'cannot be less than 0')
    
    J = np.arange(N)
    rotational_contribution = np.sum((2 * J + 1) 
                                     * np.exp((-h * c * rotational_constant * J * (J + 1))
                                      / (k * temperature)))
    return rotational_contribution

























