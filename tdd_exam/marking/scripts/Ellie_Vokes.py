# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    This determines the pressure of an ideal gas with a certain number of moles, at a specific temperature, occupying a certain voulme
    
    Parameters:
        number_of_moles(float): the number of moles of gas in the system
        temperature(float): the temperature of the system
        volume(float): the volume the system occupies
    
    Returns:
        pressure(float): the pressure of the system

    """
    if temperature < 0:
        raise ValueError('the temperature must be greater than the unphysical temperature of 0K')
    if number_of_moles < 0:
        raise ValueError('the number of moles of gas must be greater than 0')
    if volume < 0:
        raise ValueError('the volume of the system must be greater than 0m^3')
    else:
        pressure = ((number_of_moles * R * temperature) / volume)
    return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    This tells you whether a transition between two vibrational energy levels is allowed or not
    
    Parameters:
        v_0(int): the initial vibrational energy level
        v_1(int): the final vibrational energy leve;
    
    Returns:
        allowed(bool): whether the transition between vibrational energy levels in allowed
    """
    deltaV = v_1 - v_0
    
    if not isinstance(v_0, int):
        raise TypeError('the initial vibrational energy level (v_0) must be an integer')
    if not isinstance(v_1, int):
        raise TypeError('the final vibrational energy level (v_1) must be an integer')    
    if v_0 < 0:
        raise ValueError('the inital vibrational energy level (v_0) must be greater or equal to 0')
    if v_1 < 0:
        raise ValueError('the final vibrational energy level (v_1) must be greater or equal to 0')    
       
    if deltaV == 1:
        return True 
    
    if deltaV == -1:
        return True
    
    else:
        return False 

 # Function for coulomb

from scipy.constants import epsilon_0
import math
from math import pi

def coulomb(r, q_i, q_j):
    """
    Calculates the potential energy of two charged particles at a certain seperation
    
    Parameters:
        r(float): the seperation of the charged particles 
        q_i(int): the charge of particle i
        q_j(int): the charge of particle j
    
    Returns:
        potential_energy(float): the potential energy of the seperation of two charged particles 
    """
    if not isinstance(q_i, int):
         raise TypeError('the charge of particle i (q_i) must be an integer')
    if not isinstance(q_j, int):
         raise TypeError('the charge of particle j (q_j) must be an integer')
    else:
        q_i = float(q_i)
        q_j = float(q_j)
        r = np.array(r)
        potential_energy = ((q_i * q_j) / (4 * pi * epsilon_0 * r))
    return potential_energy
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    This calculates the 'goodness of fit' of the model data to the experimentally collected data
    
    Parameters:
        model(float): the model data
        exp(float): the data collected experimentally
        exp_uncertainty(float): the uncertainty in the experimental data
        
    Returns:
        chi_squared(float): the 'goodness of fit' of the model data to the experimentally collected data
    """
    exp = np.array(exp)
    model = np.array(model)
    exp_uncertainty = np.array(exp_uncertainty)
    
    if len(model) != len(exp):
        raise ValueError('there is a value missing from  the experimental data set')
    if len(model) != len(exp_uncertainty):
        raise ValueError('there is a value missing from the model data set')  
    if len(exp) != len(exp_uncertainty):
        raise ValueError('there is a value missing from  the uncertainty in experimental data')
    
    else:
        chi_squared = np.sum(((exp - model) / exp_uncertainty) ** 2)
    
    return chi_squared


# Function for partition
from scipy.constants import h, c, k
import math

def partition(N, rotational_constant, temperature):

    """
    Calculates the rotational contribution to the molecular partician function given the energy levels, rotational constant
        for the molecule and the temperature
    
    Parameters:
        N(int): energy levels 
        rotational_constant(float): the rotational constant of the molecule in cm-1 
        temperature(float): the temperature of the system in kelvin
    
    Returns:
        qR(float): the rotational contribution to the molecular partician function
    """
    J = np.arange(0, N+1)
    
    rotational_constant = rotational_constant * 100 #convert from cm-1 to m-1
    
    if not isinstance(N, int):
        raise TypeError('the energy level number (N) must be given as an integer')
    if temperature < 0:
        raise ValueError('the temperature must be greater or equal to 0 degrees celsius (-273k)')
    if rotational_constant < 0:
        raise ValueError('the rotational constant (B) must be greater than or equal to 0')
    else:
        qR = np.sum(((2 * J) + 1) * np.exp((- h * c * rotational_constant * J * (J + 1)) / (k * temperature)))
        
    return qR