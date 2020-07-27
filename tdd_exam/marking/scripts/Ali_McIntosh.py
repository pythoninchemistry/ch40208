# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the pressure occupied by an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of an ideal gas.
        temperature (float): Gas temperature (K).
        volume (float): Gas volume (m^3).

    returns:
        float: pressure of ideal gas (Pa)
     """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if volume < 0:
        raise ValueError("The volume is unphysical (V < 0).")
    if number_of_moles < 0:
        raise ValueError("The number of moles is unphysical (n < 0).")
    return ((number_of_moles*temperature*R)/volume)
        

# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Selection rules for the allowed transitions of quantum states.
    
    Args:
        v_0  (int): The original vibrational energy level.
        v_1 (int): The final vibration energy level.
        
    returns:
        Boolean : Whether the transition is allowed or not.
    """
    if v_0 < 0:
        raise ValueError("Energy level must be positive!")
    if v_1 < 0:
        raise ValueError("Energy level must be positive!")
    if not isinstance(v_0, int):
        raise TypeError("The original vibrational energy level must be an integer")
    if not isinstance(v_1, int):
        raise TypeError("The final vibrational energy level must be an integer")
    if v_0 - v_1 == 1:
        True
    if v_0 - v_1 == -1:
        True
    if v_0 - v_1 != 1:
        False
    if v_0 - v_1 != -1:
        False
    difference = v_0 - v_1
    return bool(difference)

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Calculating the potential energy between two charged particles
    
    Args:
        r (float, array-like): The distance of separation of the charged particles (nm).
        q_i (int): The charge on one of the particles.
        q_j (int): The charge on one of the particles. 
        
    returns:
        float : The potential energy between the two particles at that distance.
    """
    potential_difference = (q_i*q_j)/(4*np.pi*epsilon_0*np.array([r]))
    return potential_difference
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    The goodness-of-fit metric between the model and experimental data. 
    
    Args:
        model (array_like, float): The model data for the goodness-of-fit.
        exp (array_like, float): The experimental data for the goodnes-of-fit.
        exp_uncertainty(array-like, float): The uncertainty in the experimental data.
        
    returns:
        float: The value of the chi-squared goodness-of-fit
    """
    if len(model) != len(exp):
        raise ValueError("Arrays not same length!")
    if len(model) != len(exp_uncertainty):
        raise ValueError("Arrays not the same length!")
    if len(exp) != len(exp_uncertainty):
        raise ValueError("Arrays not the same length!")
    goodness_of_fit = np.sum(np.square((model - exp) / exp_uncertainty))
    return goodness_of_fit


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Equation to calculate the rotational contribution to the molecular partition function
    
    Args:
        B (float): The rotational constant for the molecule (cm^-1).
        T (float): The temperature (K).
        
    returns:
        float: The value for the rotational contribution 
     """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    if rotational_constant < 0:
        raise ValueError("The rotational constant is unphysical (B < 0).")
    if not isinstance(N, int): 
        raise TypeError("The energy levels must be an integer")
    J = np.arange(0,N+1)
    return np.sum(((2*J)+1)*np.exp((-h*c*rotational_constant*(J)(J+1))/(k*temperature)))


