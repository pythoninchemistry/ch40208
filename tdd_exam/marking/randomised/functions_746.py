# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    This calculates the pressure of an ideal gas based on
    the ideal gas equation.
    
    Parameters:
        number_of_moles (float): The number of gaseous moles
        temperature (float): Temperature in kelvin
        volume  (float): The volume of the container in m^3
        
    Returns (float): Pressure of the gas in Pa
    """
    p = (number_of_moles*temperature*R)/volume
    if temperature < 0:
        raise ValueError('The temperature cannot be less than zero')
    elif number_of_moles < 0:
        raise ValueError('The number of moles cannot be less than zero')
    elif volume < 0:
        raise ValueError('The volume must be greater than zero')
    else:
        return p 


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether a vibrational energy level transition is allowed or not.
    Parameters:
        v_0 (int): initial energy level
        v_1 (int): final energy level
    Returns (Boolean): True for allowed or false for not allowed
    """
    if not isinstance(v_0, int):
        raise TypeError('The vibrational energy level must be an integer')
    elif not isinstance(v_1, int):
        raise TypeError('The vibrational energy level must be an integer')
    elif v_0 < 0 or v_1 < 0:
        raise ValueError('The vibrational energy level must be equal to '
                         'or greater than 0')
    elif abs(v_0 - v_1) == 1:
        return True
    elif abs(v_0 - v_1) != 1:
        return False
     

# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    """
    Calculates the potential energy between two charges
    given the separation and the charges.
    
    Parameters:
        r(float): The distance between the particles 
        q_i: The charge of particle 1
        q_j: The charge of particle 2
        
    Returns (array-like, float): the separation energy for each separation
    """
    #make an array of r
    a = []
    r_array = a.append(r)
    #for one value of r
    if len(r_array) == 1:
        return (q_i*q_j)/(4*pi*epsilon_0*r)
    #for multiple values of r
    elif len(r_array) > 1:
        V_r = []
        for i in r_array:
            b = (q_i*q_j)/(4*pi*epsilon_0*i)
            V_r.append(b)
        return V_r 
  
        
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the chi-squared value for a set of experimental data
    compared to a model. 
    
    Parameters:
        model (array-like, float): model data set of values for comparison
        exp (array-like, float): experimental data with the same number of 
                                 values as the model data set
        exp_uncertainty (array-like, float): The uncertainty in the values
                                             obtained experimentally
    
    Returns (float): The chi-squared value
    """
    if len(model) != len(exp):
        raise ValueError('The length of the experimental data set '
                         'is not the same as the model data set')
    else:
        chi_squared = np.sum(((exp - model)/exp_uncertainty)**2)
        return chi_squared

# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates the rotational contribution to the total partition function
    for the first N energy levels.
    
    Parameters:
        N (int): The number of energy levels
        rotational_constant (): rotational constant for a given molecule in cm^-1 (B)
        temperature (float): Temperature in kelvin
        
    Returns (float): Rotational contribution of total partition function (q_rot)
    """
    if not isinstance (N, int):
        raise TypeError('The number of energy levels (N) must be '
                       'an integer.')
    elif rotational_constant < 0:
        raise ValueError('The rotational constant (B) must be greater '
                         'than zero.')
    elif temperature < 0:
        raise ValueError('The temperature in kelvin must be greater '
                         'than zero.')
    else:
        for j in range (0, N+1):
            q_rot = np.sum(2*j+1)*np.exp((-h*c*rotational_constant*j*(j+1))
                                          /(k*temperature))
        return q_rot