# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    This calculates the pressure of an ideal gas system from the 
    number of moles of gas (n), the temperature (T), the
    pressure (p), and the ideal gas constant (R).
    
    Parameters:
        number_of_moles(int): the number of moles of gas
        temperature(int): the temperature (K)
        volume(int): the volume of the system (m3)
    
    Returns:
        float: The calculated pressure (Pa)
    """
    if temperature<0:
        raise ValueError('Temperature cannot be a negative value')
    elif not isinstance(number_of_moles, int):
        raise TypeError('The number of moles of gas must be an integer')
    elif number_of_moles<0:
        raise ValueError('The number of moles of gas cannot be a negative value')
    elif volume<0:
        raise ValueError('The volume cannot be a negative value')
    else:
        return (number_of_moles*R*temperature)/volume 


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    This determines whether vibrational transitions are allowed or not based on 
    the difference between the original and final vibrational energy levels.
    
    Parameters:
        v_0(int): the initial vibrational energy level
        v_1(int): the final vibrational energy level
        
    Returns:
        bool: Whether the transition is allowed or not 
    """
    if v_0<0:
        raise ValueError('The vibrational energy levels are quantised and therefore'
                         'cannot be a negative value')
    elif not isinstance(v_0, int):
        raise TypeError('The vibrational energy level value must be an integer')
    if v_1<0:
        raise ValueError('The vibrational energy levels are quantised and therefore'
                         'cannot be a negative value')
    elif not isinstance(v_1, int):
        raise TypeError('The vibrational energy level value must be an integer')
    if abs(v_1-v_0)==1:
        return (True)
    else:
        return (False)
     

# Function for coulomb
from scipy.constants import epsilon_0
def coulomb(r, q_i, q_j):
    """
    This calculates the potential energy between two charged particles, as modeled
    with the Coulomb potential.
    
    Parameters:
        r(array_like, float): The seperation between the two charged particles
        q_i(int): The charge on particle i
        q_j(int): The charge on particle j
        
    Returns:
        float: The potential energy between the two particles.
    """
    if not isinstance(q_i, int):
        raise TypeError('The charge on particle i must be an integer')
    elif not isinstance(q_j, int):
        raise TypeError('The charge on particle j must be an integer')
    for a in [r]:
        return (q_i*q_j)/(4.0*np.pi*epsilon_0*a)
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    This calculates the goodness of fit between the calculated data to the experimental 
    data.
    
    Parameters:
        model (array_like, float): The calculated data
        exp (array_like, float): the experimental data
        exp_uncertainty (array_like, float): the uncertainty in the experimental data
        
    
    Returns: 
        float: the goodness of fit value (chi-squared)
    """
    if len(exp)<len(model):
        raise ValueError('All data arrays must be the same length, the experimental data'
                         'is too short.')
    elif len(model)<len(exp):
        raise ValueError('All data arrays must be the same length, the model data'
                         'is too short.')
    elif len(exp_uncertainty)<len(exp):
        raise ValueError('All data arrays must be the same length, the uncertainty'
                         'in the experimental data is too short.')
    return np.sum(((model-exp)/exp_uncertainty)**2)


# Function for partition
from scipy.constants import h, c, k
from math import exp

def partition(N, rotational_constant, temperature):
    """
    This calculated the rotational contribution to the molecular partition function for
    N energy levels.
    
    Parameters:
        N(int): The total number of energy levels.
        rotational_constant(float): The rotational constant, B, of the molecule (cm-1)
        temperature(float): The temperature of the system (K)
    
    Returns:
        float: The rotational contribution, qR, to the molecular partition function.
    """
    b=[]
    if temperature<0:
        raise ValueError('Temperature cannot be a negative value')
    elif not isinstance(N, int):
        raise TypeError('The number of energy levels must be an integer')
    elif rotational_constant<0:
        raise ValueError('The rotational constant, B, cannot be a negative value')
    for J in range(0,N+1):
        z=((2*J+1)*exp((-1*h*c*(rotational_constant*(10**2))*J*(J+1))/(k*temperature)))
        b.append(z)
    return np.sum(b)