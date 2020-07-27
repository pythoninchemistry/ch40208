# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determines the pressure of an ideal gas system
    Parameters:
       number_of_moles(float): Number of moles of the ideal gas (mol-1)
       temperature(float): Temperature of the gas (K)
       volume(float): Volume of the gas (m^3)
    Returns:
       float: Pressure of the gas (Pa)
    """
    if temperature < 0:
        raise ValueError('The temperature is unphysical (T<0K)') 
    if number_of_moles < 0:
        raise ValueError('The number of moles is unphysical (n<0mol)')  
    if volume < 0:
        raise ValueError('The volume is unphysical (v<0m^3)')
    return (number_of_moles * R * temperature)/volume 



# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
     Determines the allowed allowed quantum state transitions for 
     vibrational energy levels 
    Parameters:
       v_0(int): The original vibrational energy level 
       v_1(int): The final vibrational energy level 
    Returns:
       (boolean): describes whether the transition is allowed or not allowed 
    """
    if v_0 < 0:
        raise ValueError('The original vibrational energy level cannot be lower than 0')
    if not isinstance(v_0, int):
        raise TypeError("The original vibrational energy level must be an integer")
    if v_1 < 0:
        raise ValueError('The final vibrational energy level cannot be lower than 0')
    if not isinstance(v_1, int):
        raise TypeError("The final vibrational energy level must be an integer")   
    if (v_0 + v_1) == 1 or (v_0 - v_1) == -1 or (v_0 - v_1) == 1:
        return True 
    else:
        return False 
     

        
# Function for coulomb
from scipy.constants import epsilon_0
from numpy import pi 

def coulomb(r, q_i, q_j):
    """
    Determines the potential energy betweeen two particles
    Parameters:
       r(float): seperation distance between particles (cm-3)
       q_i(float): charge on particle 1 (J)
       q_j(float): charge on particle 2 (J)
    Returns:
       array_like, float: The potential energy 
    """
    return (q_i * q_j)/(4 * pi * epsilon_0 * r)
        
    
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the goodness-of-fit parameter (chi squared) of some data 
    Parameters: 
        model(array_like, float):Model data   
        exp(array_like, float): Experimental data points 
        exp_uncertainty(array_like, float): Uncertainty in the experimental data points
    Returns: 
        array_like, float: chi squared
    """
    return np.sum(np.square((exp - model) / exp_uncertainty))



# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution 
    Parameters:  
         N(int): Energy Levels 
         rotational_constant(float): The value of B, the rotational constant
                                     for the molecules (cm-1)
         temperature(float): Temperature of the molecule (K)                          
                           
    Returns: the rotational contribution to the molecular partition 
    """
    rotational_constant, temperature = int(input("Please define the units for the roational constant (cm-1)                                  and the temperature (K). "
                       "For units of cm-1 and K input 1, for anything else input 2. "           if rotational_constant, temperature == 1:
       return np.sum(np.exp((-h * c * rotational_constant )/k * temperature)) 
    else: 
       print("Warning! The units for these values are invalid, try again!")              
    if rotational_constant < 0:
        raise ValueError('The rotational constant is unphysical (B<0cm-1)')
    if temperature < 0:
        raise ValueError('The temperature is unphysical (T<0K)')
    if not isinstance(N, int):
        raise TypeError("The energy level (N) must be an integer")
          
     return np.sum(np.exp((-h * c * rotational_constant )/k * temperature))
                      
      












