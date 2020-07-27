# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the pressure for a gas, assuming ideal behaviour.
    
    Parameters:
    
        number_of_moles (float): Number of moles of gas
        temperature (float): Temperature of gas, in Kelvin
        volume (float): Volume of gas, in cubic metres
        
    Returns:
    
        p (float): Pressure of gas, in Pascals
        
    """
    if temperature <= 0:
        raise ValueError('Unphysical temperature used. Temperature '
                         'must be greater than 0 K')
    if number_of_moles < 0:
        raise ValueError('Number of moles cannot be negative')
    if volume < 0:
        raise ValueError('Volume of gas cannot be negative')
    
    p = (number_of_moles * R * temperature) / volume
    return p


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether a transition between vibrational 
    energy levels is allowed or not.
    
    Parameters:
    
        v_0 (int): Initial vibrational energy level
        v_1 (int): Final vibrational energy level
        
    Returns:
    
        boolean: Determination of whether the transition is allowed.
        
    """
    import numpy as np
    
    if type(v_0) != int:
        raise TypeError('Initial vibrational level must be an integer')
    if type(v_1) != int:
        raise TypeError('Initial vibrational level must be an integer')
    if v_0 < 0:
        raise ValueError('Cannot have a negative vibrational level')
    if v_1 < 0:
        raise ValueError('Cannot have a negative vibrational level')    
    if np.sqrt(np.square(v_1 - v_0)) == 1:
        return True
        print('Transition allowed')
    else:
        return False 
        print('Transition not allowed')

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Calculates the potential energy between two ions, of specific
    charges, separated at a given distance.
    
    Parameters:
    
        r (array): Separation(s) between ions, in metres
        q_i (float): Charge of first ion
        q_j (float): Charge of second ion
        
    Returns:
    
        array: Potential energy(-ies) between ions.
        
    """
    import numpy as np
    
    V_r = np.array((q_i * q_j) / (4 * np.pi * epsilon_0 * np.array(r)))
    
    return V_r
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculates the chi-squared value, as a "goodnes-of-fit" measurement,
    for a data set.
    
    Parameters:
    
        model (float): Value of variable predicted by model.
        exp (float): Value of variable recorded experimentally.
        exp_uncertainty (float): Error in value recorded experimentally.
        
    Returns:
    
        float: "Goodness-of-fit" measurement
        
    """
    import numpy as np
    
    if len(np.array(model)) != len(np.array(exp)):
        raise ValueError('Number of experimental and model data points '
                         'are not equal')
    if len(np.array(exp)) != len(np.array(exp_uncertainty)):
        raise ValueError('Number of experimental data points and their '
                         'uncertainties are not equal')
    if len(np.array(model)) != len(np.array(exp_uncertainty)):
        raise ValueError('Number of model data points and experimental '
                         ' uncertainties are not equal')
        
    chi_squared = np.sum(np.square((np.array(exp) - np.array(model)) / np.array(exp_uncertainty)))
    
    return chi_squared


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates the rotational contribution to the molecular
    partition function.
    
    Parameters:
    
        N (int): Energy level number
        rotational_constant (float): Rotational constant for the molecule, in cm-1
        temperature (float): Temperature of system, in Kelvin
        
    Returns:
    
        float: Rotational contribution to the molecular partition function.
        
    """
    
    import numpy as np
    
    if type(N) != int:
        raise TypeError('Number of energy levels must be equal to an integer')
    if rotational_constant < 0:
        raise ValueError('Rotational constant cannot be negative')
    if temperature <= 0:
        raise ValueError(' Temperature must be greater than 0 K')
    
    # In order for the units to cancel correctly in the equation,
    # the rotational constant needs to be in units, m^-1, as opposed to cm^-1.
    b = rotational_constant
    j = np.arange(N + 1)
    q = np.sum((2 * j + 1) * np.exp((-1 * h * c * (b * 100) * j * (j + 1)) / (k * temperature)))
    return q