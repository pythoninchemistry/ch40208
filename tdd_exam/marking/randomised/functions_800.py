# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determines the volume occupied by an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        pressure (float): Gas pressure (Pa).
    
    Returns:
        float: volume occupied (m^3).
    """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0K).")
    if number_of_moles < 0:
        raise ValueError('Unphysical number of Moles (n < 0 mol).')
    if volume < 0:
        raise ValueError('The volume is unphysical (V< 0 m^3).')
    return number_of_moles * R * temperature / volume

   
# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    '''
    Determines whether transitions are allowed between vibrational energy levels
    
    Args:
        v_0 (int): original vibrational energy level
        v_1 (int): final vibrational energy level
    Returns:
        Boolean: Whether transition is allowed or not
    '''
    if v_0 < 0 or v_1 < 0:
        raise ValueError('v_0 and v_1 must be greater than or equal to zero.')
    if not isinstance(v_0, int) or not isinstance(v_1, int):
        raise TypeError('v_0 and v_1 must be integers.')
    if (v_1-v_0) == 1 or (v_1-v_0) == -1:
        return True
    else:return False
    
# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    '''
    Determines the potential energy (Vr) between two charged particles at separation r
    
    Args:
        r (float): distance between charged particles
        q_i (int): charge on particle i
        q_j (int): charge on particle j
    
    Returns:
        float: Potential energy
    '''
    qi = np.array(q_i)
    qj = np.array(q_j)
    return (qi*qj)/(4*np.pi*epsilon_0*r)
            
#Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    '''
    determines chi squared value between experimental and model data
    
    Args:
        model (array): model data
        exp (array): experimental data
        exp_uncertianty  (array): experimental uncertainty
    Returns:
        Chi squared (float): the chi squared value
    '''
    if len(exp) < 3 or len(model) < 3 or len(exp_uncertainty) < 3:
        raise ValueError('length of data arrays should be the same length.')
    return (np.sum((exp - model)/ exp_uncertainty))**2

#Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    '''
    determines the rotational contribution to the partition 
    function from the first N energy levels
    
    Args:
        N (int): number of energy levels
        rotational_constant (float): rotational constant (cm^-1)
        temperature (float): temperature in Kelvin
    Returns:
        q_r (float): rotational contribution to the partition 
    function
    '''
    if temperature < 0:
        raise ValueError('The temperature is unphysical (T < 0K).')
    if rotational_constant < 0:
        raise ValueError(' B is unphysical (B < 0cm^-1).')  
    if not isinstance(N, int):
        raise TypeError('N must be an integer.')
    #creating J values
    J=np.array([0,N])
    #converting cm^-1 to m^-1
    B_m = rotational_constant*100
    return np.sum(((2*J)+1)*np.exp((-h*c*B_m*J*(J+1))/(k*temperature))) 
    #cant seem to get correct answer, but value errors work. sorry :(