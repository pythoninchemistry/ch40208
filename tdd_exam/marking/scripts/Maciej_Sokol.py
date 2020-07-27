# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
     Determine the pressure exerted by an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        volume (float): Volume the gas occupies (m^3).
    
    Returns:
        float: pressure exerted by the gas (Pa).
    """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if number_of_moles < 0:
        raise ValueError("The number of moles of gas is unphysical (n < 0).")
    if volume < 0:
        raise ValueError("The volume the gas occupies is unphysical (V < 0).")
        
    return number_of_moles * R * temperature / volume

   


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether a vibrational transition is allowed or not
    
    Args:
        v_0 (int): The initial vibrational energy level
        v_1 (int): The energy level that the intial vibrational level transitions to
    
    Returns:
         Boolean: Describes whether the transition is allowed or not with True or False statements
    """
    
 
    if not isinstance(v_0, int):
        raise TypeError('The initial vibrational level '
                        'must be an integer')
    if not isinstance(v_1, int):
        raise TypeError('The transition energy level '
                        'must be an integer')
    if v_0 < 0:
        raise ValueError("The initial vibrational energy level is unphyscial (v_0 < 0.")
    if v_1 < 0:
        raise ValueError("The transition energy level is unphyscial (v_1 < 0.")
        
    if v_1 == (v_0+1) or v_1 == (v_0-1):
        return True
    if v_1 != (v_0+1) or v_1 != (v_0-1): 
        return False
    
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Determines the potential energy between two particles 
    
    Args:
        r (float): Separation between particles 
        q_i (int): Charge of particle i
        q_j (int): Charge of particle j
    
    Returns:
        v(float): Potential energy between particles i and j
    """
    
    v = ((q_i * q_j)/(4 * np.pi * epsilon_0 * np.array(r)))
    
    return v
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines the goodness of fit parameter of a set of experimental data 
    
    Args:
        model (array-like, float): Model data points
        exp (array-like, float): Experimental data points
        exp_uncertainty (array-like, float): Uncertainty in the experimental data points
        
    Returns:
        chi_squared (float): The goodness of fit parameter of the experimental data points
    """
    
    chi_squared = np.sum(np.square((
        model - exp) / exp_uncertainty))
    
    return chi_squared
    

# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Determines the rotational contribution to the total partition function from the 
    first 𝑁 energy levels of a molecule
    
    Args:
        N (int): The energy level to which the summation reaches
        rotational_constant (float): The rotational constant for the molecule (cm-1)
        temperature (float): The temperature of the system (K)
    
    Returns:
        Rotational contribution (float): The rotational contribution to the total partition
        function from the first N energy levels
    """
    if not isinstance(N, int):
        raise TypeError('The energy level '
                        'must be an integer')
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    
    if rotational_constant < 0:
        raise ValueError("The rotational constant is unphysical (rotational_constant < 0).")
       
    
    i = 0
    while i <= N:
        q_r = (2 * i + 1) * np.exp(-(h * c * rotational_constant * i *( i + 1)) / k * temperature)
        return q_r
    i = i + 1
    
    return np.sum(q_r)
   
 