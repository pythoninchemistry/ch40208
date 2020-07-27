# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Function to calculate the pressure of an ideal
    gas, using the ideal gas equation.
    
    Args:
    number_of_moles(float): the number of moles of gas 
        in the system.
    temperature(float): the temperature, in Kelvin, of 
        the system.
    volume(float): the volume of gas in the system in m^-3.
    
    Return:
    pressure(float): the pressure of the gas in the system.
    """
    if temperature <0:
        raise ValueError('The temperature must be equal to or greater than 0K')
    if number_of_moles <= 0:
        raise ValueError('The number of moles must be greater than 0')
    pressure = (number_of_moles * R * temperature) / volume
    if pressure <0:
        raise ValueError('The pressure can not be negative')
    return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """ 
    A function to describe whether a vibrational transition
    is allowed from the vibrational selection rule.
    
    Args:
        v_0 (int): the initial vibrational energy level.
        V_1 (int): the final vibrational energy level.
    Return:
        Bool: True(allowed)/False(not-allowed).
     """
    if v_0 <0 :
        raise ValueError('The v_0 can not have a negative value')
    if v_1 <0 :
        raise ValueError('The v_1 can not have a negative value')
    if not isinstance (v_1, int):
        raise TypeError('v_1 must be an integer')
    if not isinstance (v_0, int):
        raise TypeError('v_0 must be an integer')
        
    delta_v= v_0 - v_1
    if delta_v == 1:
        return True
    if delta_v == -1:
        return True
    else:
        return False 
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    A function to give the potential energy between two charged
    particles, using the Coulomb potential.
    
    Args:
        r(int):A single value or list, of interatomic distances.
        q_i(int): The charge on partical 'i'
        q_j(int): The charge on partical 'j'
    Return:
        float: The potential energy of the two particals 
    """
    dist= np.array([r])
    for r in dist:
        return (q_i*q_j)/(4*np.pi*epsilon_0*r)
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    A function which calculates the 'goodness-of-fit'
    of experimental data to data from a model.
    
    Args:
        model(array): Array of the model data.
        exp(array): Array of the experimental data.
        exp_uncertainty(array): Array of the uncertainity values 
            associated with the experimental data.
     Return:
         Array: The goodness-of-fit
        
    """
    if len(model) != len(exp) != len(exp_uncertainty):
        raise ValueError
        
    return np.sum(((exp-model)/exp_uncertainty)**2)


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    A function to describe the rotational contribution to the molecular 
    partition function.
    
    Args:
        N(int): The value of the vibrational level
        rotational_constant(float): A constant given in cm^-1
        temperature(float): The temperature of the system given in K.
    Return:
        Float: The total rotational contribution to molecular partition function.
    """
    
    B= rotational_constant*100
    #conversion from cm^-1 to m-1
    
    T= temperature
    
    if rotational_constant <0:
        raise ValueError('The rotational constant must be a positive value')
    if temperature < 0:
        raise ValueError('The temperature must have a positive value')
    if not isinstance (N, int):
        raise TypeError('N must be an integer')
    
    J = np.arange(N+1)
    
    q= np.sum((2*J+1)*np.exp((-h*c*B*J*(J+1))/(k*T)))
 
   
    return q

