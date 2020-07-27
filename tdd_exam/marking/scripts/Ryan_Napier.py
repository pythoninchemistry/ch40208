# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the pressure of an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        volume (float): Volume of gas (m^3).
    
    Returns:
        float: Pressure of gas (pa).
    """
    #checking for value errors
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0K).")
    if number_of_moles < 0:
        raise ValueError("The number of moles is unphysical (n < 0).")
    if volume < 0:
        raise ValueError("The volume is unphysical (V < 0).")
    
    #if no values errors, calculate pressure and return value
    return (number_of_moles * R * temperature)/volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determine if a vibrational transition is allowed or not.
    
    Args:
        v_0 (int): Original vibrational energy level.
        v_1 (int): Fianl vibrational energy level.
        
    Returns:
        Bool: True if transition allowed, False if transition not allowed.
    """
    #checking for value and type errors
    if v_0 <= 0 or v_1 <= 0:
        raise ValueError("The vibrational energy levels must be greater than 0.")
    if not isinstance(v_0, int):
        raise TypeError("The vibrational energy levels must be an integer.")
    if not isinstance(v_1, int):
        raise TypeError("The vibrational energy levels must be an integer.")
    
    #determining if transition is allowed or not
    allowed = bool(False)
    diff = v_0 - v_1
    if diff == 1 or diff == -1:
        allowed = bool(True)  
    return allowed
     
# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Find the Coulomb potential between two charged particles.
    
    Args: 
        r (array_like, float): Distance(s) between particles (Ã…).
        q_i (float): charge on particle 1.
        q_j (float): charge on particle 2.
    
    Returns:
        array_like, float: Coulomb potential for each fo the distances (J).
    """
    #making r and numpy array so function works for both single value and array
    r = np.array(r)
    #calculating coulomb potential(s)
    coul = (q_i * q_j)/(4* np.pi * epsilon_0 * r)
    return coul
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Find the chi squared value from a set of experimental data.
    
    Args: 
        model (array_like): model used to fit data against.
        exp (array_like): experimental values.
        exp_uncertainty (array_like): error in experimental values.
    
    Returns:
        float: Chi squared value for data.
    """
    #Get lengths of arrays for model, experiment and uncertainties
    model_length = len(model)
    exp_length = len(exp)
    exp_uncert_length = len(exp_uncertainty)
    #Test lengths of arrays are the same
    if model_length == exp_length == exp_uncert_length:   
        return np.sum(np.square((exp - model)/exp_uncertainty))
    #Raise value error if not the same
    else:
        raise ValueError("The input arrays must be the same length")


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Find the rotational contribution to the partition function 
    from first N energy levels.
    
    Args: 
        N (int): Number of energy levels.
        rotational constant (float): Rotational constant, B, for molecule (cm^-1).
        temperature (float): Temperature (K).
    
    Returns:
        float: rotational contribution to the partition function, qR
    """
    #Test inputs for type and value errors
    if not isinstance(N, int):
        raise TypeError("The number of energy levels must be an integer.")
    if rotational_constant <= 0:
        raise ValueError("The rotational constant must be greater than 0.")
    if temperature <= 0:
        raise ValueError("The temperature must be greater than 0.")
    #convert the rotational constant, B, into units of m^-1
    rot_const_conv = rotational_constant*100
    q_R = 0
    #Use loop to sum rotational contribution for all energy levels
    #(N+1) used a python starts at zero
    for i in range(0,(N+1)):
        q_R = q_R + (2*i + 1) * np.exp((-h * c * rot_const_conv * i * (i+1)) / (k * temperature))
    return q_R
