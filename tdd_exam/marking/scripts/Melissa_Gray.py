# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the pressure occupied by an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K)
        volume (float): volume occupied (m^3)
    
    Returns:
        pressure(float): Gas pressure (Pa)
    """
    
    if temperature < 0:
        raise ValueError('The temperature is unphysical (T < 0 K).')
    if number_of_moles < 0:
        raise ValueError('The number of moles is unphysical (n < 0 mol)')
    pressure = (number_of_moles*R*temperature)/volume
    if pressure < 0:
        raise ValueError('The pressure is unphysical (p < 0 Pa)')
    return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    tells you if the vibrational transition is allowed or not
    
    Args:
        v_0(int): first vibrational energy level
        v_1(int): second vibrational energy level
    
    Returns:
     vib_difference(bool): if the vibrational energy is allowed (True) or not (False)
     
    """
    vib_difference = v_1 - v_0
    if vib_difference == 1:
        return True
    if vib_difference == -1:
        return True
    if vib_difference != 1 or vib_difference != -1:
        return False
    
    if v_1 < 0:
        raise ValueError('v_1 must be greater than 1')
    if v_0 <= 0:
        raise ValueError('v_0 must be greater or equal to 0')
       
        
    if v_1 < 0 and v_0 <= 0:
        raise ValueError('v_1 and v_0 must be greater or equal to 0')
        
    if not isinstance(v_0, int):
        raise TypeError('v_0 must be an integer')
    if not isinstance(v_1, int):
        raise TypeError('v_1 must be an integer')
                   
# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    """
    calculates the potential energy between two charged particles
    
    Args:
        r(float): distance between charged particles (A)
        q_i(int): charge of particle 1
        q_j(int): charge of particle 2
     
    Returns:
        potential energy(float): potential energy between particles (eV)
        
    """
    if isinstance (r, int):
        return (q_i*q_j)/(4*pi*epsilon_0*r)
    
    if not isinstance(r, int):
        r = np.array(r)
        return (q_i*q_j)/(4*pi*epsilon_0*r)
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    calculates the goodness of fit of experimental data compared to model data
    
    Args:
        model(float): array of model data
        exp(float): array of experimental data
        exp_uncertainty(float): array of experimental uncertainty
    
    Returns:
        chi_squared(float): the goodness of fit of the experimental data
    
    """
    return np.sum (((exp-model)/exp_uncertainty)**2)


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    calculates the rotational contribution to the partitin function from the first 
    N energy levels
    
    Args:
        N(int):
        rotational_constant(float): B (cm^-1)
        temperature(float): temperature of system (K)
        
    Returns: 
         rotational_contribution(float): rotational contribution to partition function
        
    """
    if not isinstance(N, int):
        raise TypeError (' N must be an integer')
    if rotational_constant < 0:
        raise ValueError('B is unphysical it must be greater than 0')
    if temperature < 0:
        raise ValueError('T is unphysical, it must be greater than 0')
    
    J = np.arange(0,N+1)
    # rotational constant in wrong units
    new_rotational_constant = rotational_constant * 100
    return np.sum((2*J+1)*np.exp((-h*c*new_rotational_constant*J*(J+1))/(k*temperature)))