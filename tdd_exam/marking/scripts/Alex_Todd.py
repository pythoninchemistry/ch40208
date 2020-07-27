# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    '''This function takes the parameters for an ideal gas, and returns the pressure.
    Args:
        number_of_moles (float): Number of moles of gas present
        temperature (float): Temperature in Kelvin
        volume (float): Volume in m3
    Returns:
        float: Pressure in Pa
    '''
    if number_of_moles < 0:
        raise ValueError('The number of moles must be a positive number.  You entered {}'.format(number_of_moles))
    if temperature < 0:
        raise ValueError('The temperature in K must be a positive number.  You entered {}'.format(temperature))
    if volume < 0:
        raise ValueError('The volume in m3 must be a positive number.  You entered {}'.format(volume))
    #Using ideal gas equation p = nRT/V
    pressure = (number_of_moles * R * temperature)/volume
    return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    '''This function takes the integer numbers of two vibrational energy levels, and returns a boolean of whether
    the transition between those levels is permitted
    Args:
        v_0 (int): first level
        v_1 (int): second level
    Returns:
        bool: true if v_0 - v_1 = +/- 1
    '''
    if type(v_0) != int:
        raise TypeError('The first argument must be an integer.  You entered {} of type {}'.format((v_0), type(v_0)))
    if type(v_1) != int:
        raise TypeError('The second argument must be an integer.  You entered {} of type {}'.format((v_1), type(v_1)))
    if v_0 < 0:
        raise ValueError('The first argument must not be negative.  You entered {}'.format(v_0))
    if v_1 < 0:
        raise ValueError('The second argument must not be negative.  You entered {}'.format(v_1))
    if np.abs(v_0 - v_1) == 1:
        return True
    else:
        return False 
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    ''' This function takes in the charges and separation of two particles, and returns the electrostatic potential
    between them
    Args:
        r (float/list of floats): distance(s) between pairs of particles in m
        q_i (float): charge on first particle in Coulombs
        q_j (float): charge on second particle in Coulombs
    Returns:
        float/list of floats: potential(s) between particles in J
    '''
    if np.min(r) <= 0:
        raise ValueError('Separation of particles cannot be less than or equal to zero.  You entered {}'.format(r))
    V = (q_i * q_j)/(4 * np.pi * epsilon_0 * np.array(r))
    return V
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    '''This function takes in the model values, experimental values, and experimental uncertainty for a dataset, and
    returns the chi-squared value for goodness of fit between the model and experiment
    Args:
        model (1-D array): values for data points given by model
        exp (1-D array): values for data points derived from experiment
        exp_uncertainty (1-D array): uncertainty on experimental values
    Returns:
        float: chi-squared value for dataset
    '''
    if len(model) != len(exp) or len(exp) != len(exp_uncertainty):
        if len(model) == len(exp):
            raise ValueError('The experimental uncertainty has length {} whilst the other arguments have length {}.  They\
            must all be equal in shape.'.format(len(exp_uncertainty), len(exp)))
        elif len(model) == len(exp_uncertainty):
            raise ValueError('The experimental data has length {} whilst the other arguments have length {}.  They\
            must all be equal in shape.'.format(len(exp), len(model)))
        elif len(exp) == len(exp_uncertainty):
            raise ValueError('The model data has length {} whilst the other arguments have length {}.  They\
            must all be equal in shape.'.format(len(model), len(exp)))
        else:
            raise ValueError('The entered arguments have lengths {}, {} and {} respectively.  They must all be the\
            same length.  Something has gone horribly wrong.'.format(len(model), len(exp), len(exp_uncertainty)))
    chi = (exp - model)/exp_uncertainty
    chi_squared = np.sum(chi**2)
    return chi_squared


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    '''This function returns the contribution to the molecular partition function of the first N rotational energy levels
    of a molecule with given rotational constant at given temperature.
    Args:
        N (int): Number of non ground-state energy levels to sum over (plus N = 0)
        rotational_constant (float): The rotational constant of the molecule (generally denoted B) in inverse cm
        temperature (float): Absolute temperature in K.
    Returns:
        float: rotational contribution to partition function, qR
    '''
    if type(N) != int:
        raise TypeError('N must be an integer.  You entered {}'.format(N))
    if N < 0:
        raise TypeError('N must be positive.  You entered {}'.format(N))
    if rotational_constant < 0:
        raise ValueError('Rotational Constant must be positive.  You entered {}'.format(rotational_constant))
    if temperature < 0:
        raise ValueError('Temperature must be positive.  You entered {}'.format(temperature))
    qR = 0
    for i in range(N + 1):
        exponent = (-h * c * rotational_constant*100 * i * (i + 1))/(k * temperature)
        #Factor of 100 included to account for rotational constant having units of cm-1
        qR += ((2 * i) + 1) * np.exp(exponent)
    return qR