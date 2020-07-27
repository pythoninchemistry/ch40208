# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the pressure of an ideal gas
    
    Parameters:
        number_of_moles (float): Number of moles of gas
        temperature (float): Temperature in K
        volume (float): Volume of gas in m^3
       
    Returns:
        float: Pressure (P) in Pa
    """
    P = ((number_of_moles*R*temperature)/volume)
    
    if temperature <= 0:
        raise ValueError('The temperature must be greater than 0 (in Kelvin)')
    if number_of_moles < 0:
        raise ValueError('The number of moles must be greater than 0')
    if volume < 0:
        raise ValueError('The volume must be greater than 0 (in m^3)')
    else:
        return P


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines if a transition between energy levels is allowed in vibrational spectroscopy
    
    Parameters:
        v_0 (int): Initial vibrational energy level
        v_1 (int): Final vibrational energy level
        
    Returns:
        bool: True = Allowed transition, False = Forbidden transition
    """
    if v_0 < 1:
        raise ValueError('v_0 cannot be negative')
    if v_1 < 1:
        raise ValueError('v_1 cannot be negative')
    if not isinstance(v_0, int):
        raise TypeError('v_0 must be an interger')
    if not isinstance(v_1, int):
        raise TypeError('v_1 must be an interger')
    if (v_1 - v_0) == 1:
        return bool(1)
    if (v_1 - v_0) == -1:
        return bool(1)
    else:
        return bool(0)
     

# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    """
    Determines the potential energy between two charged particles at given separation(s)
    
    Parameters:
        r (float or list): separation between the two particles
        q_i (int): charge on particle i
        q_j (int): charge on particle j
        
    Returns:
        float: Potential energy (V)
    """
    V = []
    if type(r) == list:
        length = len(r)
        for n in range(0, length):
            V.append((q_i * q_j)/(4 * pi * epsilon_0 * r[n]))
    else:
        V = (q_i * q_j)/(4 * pi * epsilon_0 * r)
    
    return V


        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the chi squared value for a range of data points
    
    Parameters:
        model (list): model data
        exp (list): experimental data
        exp_uncertainty (list): uncertainty in experimental data
        
    Returns:
        float: chi squared (chi_squared)
    """
    if (len(model) != len(exp)) and (len(model) != len(exp_uncertainty)):
        raise ValueError('The number of data points in the model data must be the same as in'
                         'the experimental data and the experimental uncertainty')
    if (len(exp) != len(model)) and (len(exp) != len(exp_uncertainty)):
        raise ValueError('The number of data points in the experimental data must be the same as in'
                         'the model data and the experimental uncertainty')
    if (len(exp_uncertainty) != len(model)) and (len(exp_uncertainty) != len(exp)):
        raise ValueError('The number of data points in the experimental uncertainty must be the same' 
                         'as in the model data and the experimental data')    
    else:
        chi_squared = sum(((exp - model) / exp_uncertainty)**2)
    
    return chi_squared


# Function for partition
from scipy.constants import h, c, k
from math import exp
def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution to the molecular partition function 
    
    Parameters:
        N (int): number of rotational energy levels
        rotational_constant (float): the rotational constant for the molecule in cm^-1
        temperature (float): temperature in K
        
    Returns:
        float: rotational contribution (rot)
    """
    rot_list = np.array(0)
    for i in range (1, N + 1):
        np.append(rot_list, ((2 * i + 1) * exp((-h * c * rotational_constant * i * (i + 1)) / k * temperature)))
                  
    rot = np.sum(rot_list)
    return rot
        
