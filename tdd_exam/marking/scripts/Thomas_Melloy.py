# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Performs a calculation to find the pressure of a gas for a given volume, temperature and number of moles
    
    Args:
    number of moles (float) = number of moles of the gas (mol)
    temperature (float) = temperature of the gas (K)
    volume (float) = volume occupied by the gas (m^3)
    
    Returns:
    pressure (float) = pressure of the gas (Pa)
    """

    if temperature < 0:
        raise ValueError ("Temperature cannot be negative in Kelvin")
        
    if number_of_moles < 0:
        raise ValueError ("Number of moles cannot be negative")
        
    if volume < 0:
        raise ValueError ("Volume cannot be negative")
        
    return (number_of_moles * temperature * R)/volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Function will tell whether or not a transition is allowed by the selection rules of vibrational spectroscopy
    
    Args:
    v_0 (int) = initial quantum state
    v_1 (int) = excited quantum state
    
    Returns:
    True = Transition is allowed
    False = Transition is forbidden
    """
    if v_0 < 0:
        raise ValueError ("values for quantum states must be positive")
    
    if v_1 < 0:
        raise ValueError ("values for quantum states must be positive")
    
    if not isinstance(v_0, int):
        raise TypeError("Values for quantum states must be integers")
        
    if not isinstance(v_1, int):
        raise TypeError("Values for quantum states must be integers")
    
    if (v_0 - v_1) == 1:
        return True
    
    if (v_0 - v_1) == -1:
        return True
    
    else:
        return False
    
    

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Function will calculate the potential energy between 2 charged particles
    
    Args:
    r (float) = separation of 2 charged particles (m)
    q_i (float) = charge on particle i (C)
    q_j (float) = charge on particle j (C)
    
    Returns:
    V(r) (float) = potential energy between the particles (J)
    """
    if isinstance (q_i, list):
        return [(q_i[0] * q_j)/(4 * np.pi * epsilon_0 * r), 
                (q_i[1] * q_j)/(4 * np.pi * epsilon_0 * r)]
    else:
        return (q_i * q_j)/(4 * np.pi * epsilon_0 * r)
    
        
    
    

    
    
    
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Function will calculate chi_squared based on data supplied in array form
    
    Args:
    model (array) = calculated theoretical values for an experiment
    exp (array) = experimental values taken from the experiment
    exp_uncertainty (array) = uncertainty in the values taken from the experiment
    
    Returns:
    chi_squared (float) = single value to show how well experimental data fits to model data
    """
    
    
    return np.sum(((exp-model)/exp_uncertainty)**2)


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates the value for the rotational contribution to the molecular partition function
    
    Args:
    N (int) = quantum state
    rotational_constant (float) = rotational constant of the molecule (cm^-1)
    temperature (float) = temperature of the molecule (K)
    
    Returns:
    qR (float) = rotational contribution to the molecular partition function
    """ 
    if temperature < 0:
        raise ValueError ("Temperature cannot be negative in Kelvin")
    if rotational_constant < 0:
        raise ValueError ("Rotational constant cannot be negative")
    if not isinstance(N, int):
        raise TypeError('N must be an integer')
    
    J = np.arange(0, (N + 1))
    
    return np.sum((2*J+1) * np.exp(-h*(c*100)*rotational_constant*J*(J+1)/(temperature * k)))









