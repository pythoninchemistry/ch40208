# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    
    """
    Determines the pressure of an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        pressure (float): Gas pressure (Pa).
    
    Returns:
        float: pressure (Pa).
    """

    if temperature < 0:
        
        raise ValueError ('Unphysical temperature - T < 0K')
    
    elif number_of_moles < 0:
        
        raise ValueError ('Unphysical number of moles - n < 0Pa')
        
    elif volume < 0:
        
        raise ValueError ('Unphysical volume - v < 0 m^3')
    
    else:
        return (number_of_moles * temperature * R) / volume


    
    
    
    
# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    
    """
    Determines whether a vibrational transition is allowed or not.
    
    Args:
        v_0: original energy level quantum number
        v_1:final energy level quantum number
        
    
    Returns:
        Boolean: describes whether the transition is allowed or not. 
    """
    if not isinstance(v_0, int):
        raise TypeError ('Original energy level (v_0) is not quantised')
        
    elif not isinstance(v_1, int):
        raise TypeError ('Final energy level (v_1) is not quantised')
    
    elif v_0 < 0:
        raise ValueError ('Original energy level (v_0) is less than 0')
    
    elif v_1 < 0:
        raise ValueError ('Final energy level (v_1) is less than 0')
    
    else:
        return (v_1 - v_0)**2 == 1






# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    
    """
    Determines potential energy (𝑉(𝑟)) between two charged particles, at a separation (𝑟).    
    
    Args:
        q_i (integer): charge on particle 1 
        q_j (integer): charge on particle 2 
        r (float): separation 
    
    Returns:
        float: Potential energy
    """
    if not isinstance(q_i, int):
        raise TypeError ('Charge on particle 1 is not an integer')
    
    elif not isinstance(q_j, int):
        raise TypeError ('Charge on particle 2 is not an integer')
    
    else:
        return((q_i * q_j) / (4 * pi * epsilon_0)) * (1/r)
   
        
        
        
        
        
    
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    
    """
    Determines the chi-squared value for a between a model and an experimental value
    
    Args: 
        model: values from the model data
        exp: values from the experimental data
        exp_uncertainty: uncertainty in the experimental data 
        
    Returns: 
        float: chi squared value
    """
    
    return sum(((model - exp)/exp_uncertainty)**2)


#add more if you have time 




# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    
    """
    Determines rotational contribution to the molecular partition function
    
    Args: 
        N: Energy level (J) 
        rotational_constant: rotational constant (B) value (cm^-1)
        temperature: Temperature (K) 
        
    Returns: 
        float: chi squared value
    """
    
    if temperature < 0:
        
        raise ValueError ('Unphysical temperature - T < 0K')
    
    elif rotational_constant < 0:
        
        raise ValueError ('Unphysical rotational constant - B < 0Pa')
        
    elif not isinstance(N, int):
        
        raise TypeError ('J value is not an integer')
    
    else:
        return sum((2*N + 1)*np.exp((-(h * c * rotational_constant*100 * N * (N+1))) / (k * temperature)))



# need to multiply either rotational constant or c by 100 in order to get correct unit conversion

# couldn't get my functions to operate on a mixture of integers and arrays/lists
















