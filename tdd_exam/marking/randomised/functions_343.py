# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the pressure of an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (in units of K).
        volume (float): Volume of an ideal gas (m^3).
    
    Returns:
        float: pressure of an ideal gas (Pa).
    """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if number_of_moles < 0:
        raise ValueError("The number of moles of an ideal gas is unphysical (n>0).")
    if volume < 0:
        raise ValueError("The volume of an ideal gas is unphysical (V>0).")
    return number_of_moles * R * temperature / volume
    return 

# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines if the vibrational energy level transition is allowed by the vibrational selection rule.
    
    Args:
    v_0 (integer): initial vibrational energy level
    v_1 (integer): final vibrational energy level
    
    Returns: 
    Boolean: True or False in regards to whether this transition is allowed (True) or disallowed (False). 
    """
    if v_1 <= 0:
        raise ValueError("Quantum number must be greater than 0.")
    if v_0 <= 0:
        raise ValueError("The principal quantum number must be greater than 0.")
    if not isinstance(v_1, int):
        raise TypeError("Quantum number must be an integer")
    if not isinstance(v_0, int):
        raise TypeError("Quantum number must be an integer")
    if v_1 - v_0 == 1:
        return(v_1 - v_0 == 1)
    if v_1 - v_0 == -1:
        return(v_1 - v_0 == -1)
    if v_1 - v_0 > 1:
        return(v_1 - v_0 == 1)
    if v_1 - v_0 != -1:
        return(v_1 - v_0 == -1)
    
        
# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    """
    Returns the potential energy between two particles when given the separation (r) and charges (q_i, q_j). 
    
    Args: 
    r (float or array): Seperation between charged particles
    q_i (integer): Charge of particle i
    q_j (integer): Charge of particle j
    
    Returns:
    Float: Potential Energy between particle i and particle j
    """
    if not isinstance(r, int):
        return (q_i*q_j)/(4*pi*epsilon_0*np.array(r))
        
    return (q_i*q_j)/(4*pi*epsilon_0*r)
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Returns calculated value for chi_sqaured - The goodness-of-fit metric between the model 
    and experimental data.
    
    Args:
    model(array_like, float): The transmittance of component 1
    exp(array_like, float): The transmittance of the mixture.
    exp_uncertainty(array_like, float): The uncertainty in transmittance of the mixture
    
    Returns:
    float: The value of the chi-squared goodness-of-fit     
    """
    chi_squared = np.sum(np.square((model - exp) / exp_uncertainty))
    return chi_squared

# Function for partition
from scipy.constants import h, c, k
import numpy as np

def partition(N, rotational_constant, temperature):
    """
    Returns the calculated value for rotational contribution to the molecular partition function (q)
    
    Args:
    N(int): Number of energy levels considered
    rotational_constant(float): Rotational constant of the molecule (converted from cm-1 to m-1 in this function)
    temperature(flaot): The temperature of the system
    
    Returns:
    float: The rotational contribution to the molecular partition function (q)
    """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if rotational_constant < 0:
        raise ValueError("The rotational_constant must be a positive value.")
    if not isinstance(N, int):
        raise TypeError("N must be an integer")
     
    q = 0
    i = 0
    while i <= N:
        q = (2*i + 1)*np.exp((-h*c*rotational_constant*(100)*i*(i + 1))/(k*temperature))
        i += 1
    return q
   
# Unit conversion for partition function to convert from units of cm-1 to m-1 x 100 for the rotational_constant
    
    
    
    
    