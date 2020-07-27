# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Function to find the pressure of a gas given the temperature, the number of moles and its volume
    
    Args:
        number of moles (float, cannot be negative)
        temperature (float, cannot be less than 0 Kelvin)
        volume (float, cannot be negative)
    
    Returns:
        Pressure (float)
    """
       
    if number_of_moles < 0:
        raise ValueError ('The number of moles cannot be less than 0')
    if temperature < 0:
        raise ValueError ('The temperature of a system cannot be negative')
    if volume < 0:
        raise ValueError ('The volume of a system cannot be negative')
    p =(number_of_moles*R*temperature)/volume

    return p


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Function that finds the allowed vibrational energy transitions avialable for any given vibrational quantum numbers
    
    Args:
        v_0 (int, must be greater than 0)
        v_1 (int, must be greater than 0)
   
   Returns:
        delta_v (bool) 
    """
    if v_0 < 0:
        raise ValueError ('The vibrational quantum number cannot be less than 0')
    elif not isinstance (v_0, int):
        raise TypeError ('The vibrational quantum number (v_0)'
                         'must be an integer')
    if v_1 < 0:
        raise ValueError ('The vibrational quantum number cannot be less than 0')
    elif not isinstance (v_1, int):
        raise TypeError ('The vibrational quantum number (v_1)'
                         'must be an integer')
    delta_v = v_1 - v_0
    if delta_v == 1 or delta_v == -1:
        delta_v = True
    else: 
        delta_v = False
    return delta_v
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Determines potential energy between two charged particles of any given charge (q_i and q_j respectively)
    using the Coloumbic interaction model.
    
    Args: 
        r (np.array(floats)) - list of different distances between the charged particles
        q_i (int) - charge on particle i
        q_j (int) - charge on particle j
        
    Returns:
        V_r (np.array(floats)) - list of differing potential energies based on r
    """
    from math import pi
    r_prime = np.array(r) 
    #so that multiple values of r can be entered (e.g. a list as per test 2) need to convert r into a numpy array (r_prime)
    # the code will then iterate through all values of r in the array and return another array containing the values of V_r
    V_r = ((q_i*q_j)/(4*pi*epsilon_0*r_prime))
    
    return V_r
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Finds the chi squared value for any data set.
    This value gives an idea of how well the experimental data fits the model data
    
    Args:
        model (np.array (floats))
        exp (np.array (floats))
        exp_uncertainty (np.array (floats))
    
    Returns:
        chi (np.array (floats))
    """ 
    
    """
    Although I have not explicitly coded to raise an error:
    If the arrays are not of equal length then an automatic error will be raised by numpy/python
    stating that the arrays are not of equal length thus fulfilling the criteria of the tests written
    """
    chi = np.sum (np.square((exp - model)/exp_uncertainty))
    return chi
   


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates the rotational contribution to the molecular partition function given the rotational constant of a molecule (B),
    The number of molecules (N) and the temperature (T)
    
    Args:
        N (int)
        rotational_constant (float) - cannot be negative in cm^-1
        temperature (float) - cannot be negative
    Returns:
        q_r (float)
    """
    if not isinstance (N, int):
        raise TypeError ('The number of molecules (N)'
                         'must be an integer')
    if rotational_constant < 0:
        raise ValueError ('The rotational constant must be greater than 0')
    if temperature < 0:
        raise ValueError ('The temperature of a system cannot be negative')
        
    J = np.arange (0, N+1) #N+1 because a range is exclusive of upper and lower values stated in brackets
    
    B = rotational_constant*100 #convert the given value of the rotational constant into ms^-1 so units match
    
    degeneracy = 2*J +1
    
    energy = h*c*B*J*(J+1)
    
    """
    From stat therm lectures know that partition function takes general form of 'q = sum (degeneracy*exp(-energy/kT)'
    So I have seperate variables for degeneracy and energy.
    This so the overall equation for q_r is easier to read (i.e. fewer brackets)
    """
    q_r = np.sum (degeneracy*np.exp(-energy/(k*temperature)))
    return q_r