# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the pressure of a gas given the number of moles, temperature and volume (assuming ideality)
    
    Args:
    
    number_of_moles: (float) The number of moles of gas
    temperature: (float) The temperature in kelvin
    volume: (float) The volume of the system in m^3
    
    Returns:
    
    p: (float) Pressure of the gas under the given conditions in newtons per m^2
    
    """
    if number_of_moles < 0:                                         #If the user enters a non-physical number of moles 
        raise ValueError('Number of moles must be greater than 0')  # the function returns a value error
    if temperature < 0:                                             # If the user enters a non-physical temperature 
        raise ValueError('Temperature must be greater than 0 K')    # the function returns a value error
    if volume < 0:                                                  # If the user enters a non-physical volume
        raise ValueError('Volume must be greater than 0')           # the function returns a value error
    else:
        p = (number_of_moles*R*temperature)/volume
    return p


# Function for vib_spec_transition

def vib_spec_transition(v_0, v_1): 
    
    delta_v = v_1-v_0
    if delta_v == 1 or delta_v == -1:
        return True
    if v_0 < 1 or v_1  < 1:
        raise ValueError('Vibrational energy levels must be positive')
    elif v_0 == float or v_1 == float:
        raise ValueError('Vibrational enery levels must be integers')
    elif delta_v == float:
        raise TypeError(ffm)
    elif delta_v == 1 or delta_v == -1:
        return True
    elif delta_v > 1 or delta_v < -1:
        return False
    elif delta_v == 0:
        return False
    

# Function for coulomb
def coulomb(r, q_i, q_j):                 
    
    """
    Calculates the vibrational energy between two particles for a given distance and charges.
    
    Args:
    
    r: (Array-like, Floats) Distance between the particles
    q_i: Charge on particle i
    q_j: Charge on particle j
    
    Returns: Array of vibrational energy levels for values of r
    
    """
    from scipy.constants import epsilon_0
    import numpy as np
    from math import pi
    v = []                                         #Empty array for inputting values of energy
    if type(r) == float or type(r) == int:         # Essentially if only one value of r is input into the function,
        v.append((q_i*q_j)/(4*pi*epsilon_0*r))     # This will be satisfied and calculate one value 
    else:                                          #Otherwise an array of values of r has been input, so calculate 
         for d in r:                               # Values of V for each value of r and append them into the empty array
            v.append((q_i*q_j)/(4*pi*epsilon_0*d))
    return v
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    
    """
    Calculates the Chi squared value in a given set of data
    
    Args:
    
    model: (Array-like, Floats) Y values of some model for the data
    exp: (Array-like, Floats) Y values from the experimental data
    exp_uncertainty: (Array-like, Floats) Uncertainty in experimental data points.
    
    return: (float) Chi squared
    
    
    """
    if len(model) == len(exp) == len(exp_uncertainty):    #If the length of all the arrays is equal, calculate a val
        chi_squ = np.sum((exp-model)/exp_uncertainty)**2   # For chi squared
    else:
        raise ValueError('Length of arrays not equal')    # If not all the arrays are of equal length, raise a type error.
    return chi_squ
  

# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    
    """ 
    Takes values of rotational constant, temperature and 
    
    """ 
    from math import exp
    if type(N) != int:
        raise TypeError('N must be an integer')
    elif temperature < 0:
        raise ValueError('Temperature must be a real temperature greater than 0 K')
    elif rotational_constant < 0:
        raise ValueError('Rotational constant must be greater than 0')
    else:
        for J in range(N):
            return np.sum((2*J + 1)*exp((-h*c*rotational_constant*J(J+1))/k*temperature))