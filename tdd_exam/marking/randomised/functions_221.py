# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determines the pressure of an ideal gas for a given
    number of moles, temperature, and volume.
    
    Args:
        number_of_moles (float): Number of moles of gas (mol)
        temperature (float): Temperature of gas (K)
        volume (float): Volume of gas (m^3)
    
    Returns:
        float: ideal gas pressure (Pa)
    
    """
    # Errors for unphysical values
    if temperature < 0:
        raise ValueError("Temperature is unphysical. "
                         "The temperature of gas must be greater than 0 K.")
    if number_of_moles < 0:
        raise ValueError("Number of moles is unphysical. "
                         "The number of moles of gas must be greater than 0 mol.")
    if volume < 0:
        raise ValueError("Volume is unphysical. "
                         "The volume of gas must be greater than 0 m^3.")
        
    pressure = (number_of_moles * R * temperature) / volume
    
    return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines if a vibrational transition is allowed 
    based on the energy level quantum numbers.
    
    Args:
        v_0 (int): original vibrational energy level quantum number
        v_1 (int): final vibrational energy level quantum number
        
    Returns:
        bool: whether the transition is allowed
        
    """
    
    delta_v = v_1 - v_0
    
    if type(v_0) != int:
        raise TypeError("Original energy level quantum number must be an integer.")
    if type(v_1) != int:
        raise TypeError("Final energy level quantum number must be an integer.")
    if type(v_1) and type(v_0) != int:
        raise TypeError("Both the Original and Final energy level "
                        "quantum numbers must be integers.")
    if v_0 < 0:
        raise ValueError("Original energy level quantum number must be greater than 0.")
    if v_1 < 0:
        raise ValueError("Final energy level quantum number must be greater than 0.")
    if v_0 and v_1 < 0:
        raise ValueError("Original and Final energy level "
                         "quantum numbers must be greater than 0.")
    
    allowed = True
    
    if delta_v == 1:
        allowed = True
    if delta_v == -1:
        allowed == True
    if delta_v > 1:
        allowed = False
    if delta_v < -1:
        allowed = False
   
    return allowed
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Determines the potential energy between two charged particles
    for a given separation, based on a Coulomb potential model
    
    Args:
        r (array_like or single value, float): separation between charged particles
        q_i (int): charge of particle i
        q_j (int): charge of particle j
        
    Returns:
        array_like or single value, float: potential energy 
    """
    if np.array(r).size == 1:
        V_r = (q_i * q_j) / (4 * np.pi * epsilon_0 * r)
    if np.array(r).size > 1:
        r_array = np.array(r)
        V_r = (q_i * q_j) / (4 * np.pi * epsilon_0 * r_array)
    
    return V_r
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the chi_squared "goodness of fit" parameter 
    between experimental data and a model
    
    Args:
        model (array_like, float): model data points
        exp (array_like, float): experimental data points
        exp_uncertainty (array_like, float): uncertainty for experimental data points
        
    Returns:
        float: chi_squared value for model data and experimental data
    """
    # Length of arrays
    N_m = model.size
    N_exp = exp.size
    N_uncert = exp_uncertainty.size
    
    if N_m == N_exp == N_uncert:
        chi_squared = np.square(np.sum((exp - model) / exp_uncertainty))
    if N_exp < N_m and N_uncert:
        raise ValueError("Experimental data has too few values compared to uncertainty "
                         "and model data.")
    if N_m < N_exp and N_uncert:
        raise ValueError("Model data has too few values compared to uncertainty "
                         "and experimental data.")
    if N_uncert < N_m and N_exp:
        raise ValueError("Uncertainty data has too few values compared to experimental "
                         "and model data.")
        
    return chi_squared


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution to the molecular
    partition function 
    
    Args:
        rotational_constant (float): rotational constant for the molecule (cm^-1)
        temperature (float): temperature (K)
        N (int): number of energy levels
    
    Returns:
        float: rotational contribution to molecular partition function
    
    """
    
    if type(N) != int:
        raise TypeError("N must be an integer value.")
    if rotational_constant < 0:
        raise ValueError("Rotational constant, B, is unphysical - "
                         "it must be greater than 0 cm^-1.")
    if temperature < 0:
        raise ValueError("Temperature is unphysical - it must be greater than 0 K.")
        
    J = np.arange(N+1)
    
    # converting c into cms^-1 from ms^-1 within the equation
    q_R = np.sum((2 * J + 1) * 
                 np.exp((-h * c * 100 * rotational_constant * J * (J + 1)) / (k * temperature)))
    
    return q_R
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    