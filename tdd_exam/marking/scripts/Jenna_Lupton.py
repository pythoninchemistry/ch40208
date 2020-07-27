# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determines the pressure of an ideal gas, using the ideal gas law
    given the volume, temperature and number of moles of the ideal gas.
    
    Parameters:
        number_of_moles (float): The number of moles of the ideal gas
        temperature (float): The temperature of the ideal gas
        volume (float): The volume of the ideal gas
        
    Returns:
        float: The pressure of the ideal gas
    """
    if temperature < 0:
        raise ValueError ('The temperature cannot be unphyiscal; it must be '
                          'greater than or equal to 0 K')
    elif number_of_moles < 0:
        raise ValueError ('The number of moles of gas cannot be unphyiscal; '
                          'it must be greater than or equal to 0 mol')
    elif volume < 0:
        raise ValueError ('The volume cannot be unphysical; it must be greater '
                          'than or equal to 0 m3')
    else:
        pressure = (number_of_moles * R * temperature) / volume
        return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether a transition between two vibrational energy levels is
    allowed or not, given the initial and final vibrational energy levels.
    
    Parameters:
        v_0 (int): The initial vibrational energy level
        v_1 (int): The final vibrational energy level
        
    Returns:
        boolean: Describes whether the vibrational transition is allowed or not
    """
    if not isinstance (v_0, int):
        raise TypeError ('The energy levels are quantised, therefore, they '
                         'must be integer values')
    elif not isinstance (v_1, int):
        raise TypeError ('The energy levels are quantised, therefore, they '
                         'must be integer values')
    elif v_0 < 0:
        raise ValueError ('The energy level must be greater than or equal to 0')
    elif v_1 < 0:
        raise ValueError ('The energy level must be greater than or equal to 0')
    else:
        delta_v = v_1 - v_0
        if delta_v == 1 or delta_v == -1:
            return True
        else:
            return False


# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Determines the potential energy between two particles when given the separation
    between them and their charges.
    
    Parameters:
        r (float or list): The separation between the two particles
        q_i (int): The charge of the first particle
        q_j (int): The charge of the second particle
        
    Returns:
        float: The potential energy between the two particles
    """
    r = np.array(r)
    potential_energy = (q_i * q_j) / (4 * np.pi * epsilon_0 * r)
    return potential_energy

    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the chi-squared value, the goodness-of-fit, between the experimental
    data set and the model data set.
    
    Parameters:
        model (array): The model data set
        exp (array): The experimental data set
        exp_uncertainty (array): The experimental uncertainty in the measurement of
                                 the experimental data set
                                 
    Returns:
        float: The value of chi-squared, the goodness-of-fit, between the experimental
               and model data sets
    """
    if len(model) != len(exp):
        raise ValueError ('The arrays must be of the same length to be able to do '
                          'multiplication and division')
    elif len(model) != len(exp_uncertainty):
        raise ValueError ('The arrays must be of the same length to be able to do '
                          'multiplication and division')
    elif len(exp) != len(exp_uncertainty):
        raise ValueError ('The arrays must be of the same length to be albe to do '
                          'multiplication and division')
    else:
        chi_squared = np.sum(((exp - model) / exp_uncertainty) ** 2)
        return chi_squared


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution to the molecular partition function for
    the first N energy levels, given values of N, the rotational constant B, and the
    temperature.
    
    Parameters:
        N (int): The total number of energy levels
        rotational_constant (float):The rotational constant for the molecule, B,
                                    with units of cm-1
        temperature (float): The temperature with units of K
        
    Returns:
        float: The rotational contribution to the molecular partition function for
               the first N energy levels
    """
    if not isinstance (N, int):
        raise TypeError ('The value of N must be an integer')
    elif rotational_constant < 0:
        raise ValueError ('The rotational constant, B, cannot be unphysical; it must '
                          'be greater than or equal to 0 cm-1')
    elif temperature < 0:
        raise ValueError ('The temperature cannot be unphysical; it must be greater than '
                          ' or equal to 0 K')
    else:
        B = rotational_constant * 100
        rot_contribution = 0
        for J in range(0, N + 1):
            q_R = (2 * J + 1) * np.exp((-h * c * B * J * (J + 1)) / (k * temperature))
            rot_contribution += q_R
        return rot_contribution
