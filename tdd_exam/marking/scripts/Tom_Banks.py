# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Uses the ideal gas law to calculate pressure of an ideal gas.
        
    Args:
        number_of_moles (float or int): The number of moles of gas
        
        temperature (float or int): The temperature of the system in Kelvin
        
        volume (float or int): The volume of the system in dm^-3
        
    Returns:
        pressure (float): The pressure of the gas in this system, in Pascals  
    """
    #Check that values for temperature, pressure and moles are
    #physically possible (i.e. > 0):
    if temperature < 0:
        raise ValueError("Temperature must be >= 0, negative temperatures in"
                         "Kelvin are unphysical")
    
    if number_of_moles < 0:
        raise ValueError("The number of moles of gas must be >= 0")
        
    if volume < 0:
        raise ValueError("The pressure must be a positive value")
    
    #Calculate the pressure:
    else:
        pressure = (number_of_moles * R * temperature) / volume
        
    return pressure 


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether a transition between vibrational quantum states is allowed
    based on the vibrational spetroscopy selection rule.
    
    Args:
        v_0 (int): The original vibrational energy level
        
        v_1 (int): The final vibrational energy level
        
    Returns: 
        Bool: Whether the transition is allowed or disallowed,
              True for allowed and False for disallowed
    """
    #Check that the energy levels given are physically possible, 
    #i.e. that they are positive and integers.
    if not isinstance(v_0, int) or not isinstance(v_1, int):
        raise TypeError("The vibrational energy levels must be given as integers.")
    
    if v_0 < 0 or v_1 < 0:
        raise ValueError("The vibrational energy levels must be positive.")
        
    #Accommodate for allowed transitions (i.e. delta v = +-1)
    if v_0 - v_1 == 1:
        Transition_allowed = True
        
    elif v_1 - v_0 == 1:
        Transition_allowed = True
    
    #Any other transitions break the selection rule and therefore 
    #are disallowed
    else: 
        Transition_allowed = False
    
    return Transition_allowed
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Returns the potential energy between two charged particles.
    
    Args:
        r (float): The separation between the charged particles
       
        q_i (float): The charge of particle 1
        
        q_j (float): The charge of particle 2
        
    Returns: 
        potential_energy (float): The potential energy calculated
    """
    #Calculate numerator and denominator separately
    numerator = q_i * q_j
    
    denominator = 4.0 * np.pi * epsilon_0 * r
    
    #Combine to give potential_energy
    potential_energy = numerator / denominator

    return potential_energy
    
    #Unfinished - trying to distinguish between float and array inputs
    #if type(r) == float:
        #denominator = 4.0 * np.pi * epsilon_0 * r
    
        #Combine to give potential_energy
       # potential_energy = numerator / denominator
    
       # return potential_energy
   # else:
    #    denominator = np.array([4.0 * np.pi * epsilon_0 * r])else:
    #    denominator = np.array([4.0 * np.pi * epsilon_0 * r])
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Returns the goodness-of-fit parameter (i.e. chi squared) for a model
    when compared to experimental values and their uncertainties.
    
    Args:
        model (float, array-like): The model values to be evaluated
        
        exp (float, array-like): The experimental values
        
        exp_uncertainty (float, array-like): The experimental uncertainty
                                             in the measurement of exp
    
    Returns: 
        chi_squared (float): The goodness-of-fit parameter for the model
    """
    #Check that all input arrays are equal in length
    #If they are, calulate chi squared:
    if len(model) == len(exp) == len(exp_uncertainty):
        
        chi_squared = np.sum(np.square( (exp - model)/ exp_uncertainty ))
    
    #If they aren't equal in length, return an error:
    else:
        raise ValueError("All input arrays should be of the same length")
      
    return chi_squared


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Finds the rotational contribution to the molecular partition function.
        
    Args:
        N (int): The number of energy levels (from 0) to be considered
        
        rotational_constant (float): The rotational constant, B to be 
                                     considered
        
        temperature (float): The temperature of the system
        
    Returns:
        rotational_contribution (float): The calculated rotational
                                         contribution
    """
    #Convert c into units of cm per second for compatibility with B in per cm:
    c_in_cm_per_s = c * 100
    
    #Check that values for N, B and temperature are physical, i.e. they are
    #integer (N), postive (B) and positive (temp) resectively:
    if not isinstance(N, int):
        raise TypeError("N must be an integer value")
        
    if rotational_constant < 0:
        raise ValueError("The rotational constant must be a positive number")
    
    if temperature < 0:
        raise ValueError("Temperature must be >= 0, negative temperatures in"
                         "Kelvin are unphysical")
    

    else:
    #Create values of from 0 to N:
        J = np.arange(0, N)
        
    #Calculate the rotational contribution from the equation:
        rotational_contribution = np.sum( ((2 * J) + 1) * np.exp(
                                        (-h * c_in_cm_per_s * 
                                         rotational_constant * J * (J + 1)) /
                                         (k * temperature)))
    
        return rotational_contribution