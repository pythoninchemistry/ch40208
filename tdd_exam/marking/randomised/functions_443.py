# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """Determine the pressure for a given number of moles, temperature and volume
    Args:
        number_of_moles (float): Number of moles of ideal gas
        temperature (float): Temperature of ideal gas
        volume (float): Volume of ideal gas
    Returns:
        float: The pressure of the ideal gas
    """
    
    if (type(number_of_moles)) == int or float:
        pass
    else:
        raise TypeError("number_of_moles must be int or float")
    if (type(temperature)) == int or float:
        pass
    else:
        raise TypeError("temperature must be int or float")
    if (type(volume)) == int or float:
        pass
    else:
        raise TypeError("volume must be int or float")
    if number_of_moles < 0:
        raise ValueError("number_of_moles must be positive")
    if temperature < 0:
        raise ValueError("temperature must be positive")
    if volume < 0:
        raise ValueError("volume must be positive")
    
    return (number_of_moles * temperature * R / volume)


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """Determine if a vibrational transition is allowed based on the starting energy level and final energy level
    Args:
        v_0 (int): Starting energy level
        v_1 (int): Final energy level
    Returns:
        bool: if the transition is allowed or forbidden
    """

    if (type(v_0)) != int:
        raise TypeError("v_0 must be int")
    if (type(v_1)) != int:
        raise TypeError("v_1 must be int")
    if v_0 < 0:
        raise ValueError("v_0 must be positive")
    if v_1 < 0:
        raise ValueError("v_1 must be positive")
    if abs(v_0 - v_1) == 1:
        return True
    else:
        return False
     

# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    """Calculates the potential energy between two charged particles with charges q_i and q_j at distance r
    Args:
        q_i (float): Charge on particle 1
        q_j (float): Charge on particle 2
        r (float): Distance between particles 1 and 2
    Returns:
        float: The potential energy between particles 1 and 2
    """
    
    distance = np.array(r)
    return ((q_i * q_j)/(4 * pi * epsilon_0 * distance))
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """Calculates the goodness-of-fit for an array of experimental data, experimental uncertainty and model data
    Args:
        exp (array_like): Experimental y values
        exp_uncertainty (array_like): Uncertainty in experimental y values
        model (array_like): Model y values
    Returns:
        float: Chi squared for the above data
    """
    
    if (len(model) != len(exp)):
        raise ValueError("Experimental data is not the same length as model data")
    if (len(model) != len(exp_uncertainty)):
        raise ValueError("Experimental uncertainty data is not the same length as model data")
    return np.sum(((exp - model)/(exp_uncertainty))**2)


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """Calculates the rotational contribution to the molecular partition function for a given rotational constant, temperature and maximum energy level
    Args:
        N (int): Maximum energy level
        rotational_constant (float): Rotational constant
        temperature (float): Temperature
    Returns:
        float: Rotational contribution to the molecular partition function
    """
    if (type(N)) != int:
        raise TypeError("N must be int")
    if (type(temperature)) == int or float:
        pass
    else:
        raise TypeError("temperature must be int or float")
    if (type(rotational_constant)) == int or float:
        pass
    else:
        raise TypeError("rotational_constant must be int or float")
    if N < 0:
        raise ValueError("N must be positive")
    if rotational_constant < 0:
        raise ValueError("rotational_constant must be positive")
    if temperature < 0:
        raise ValueError("temperature must be positive")
    pf = 0
    for i in range(0, (N+1)):
        pf = (pf + ((2 * i + 1) * np.exp((-1 * h * c * (100 * rotational_constant) * i * (i + 1))/(k * temperature))))
    return pf