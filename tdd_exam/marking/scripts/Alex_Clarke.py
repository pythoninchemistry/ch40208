# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the pressure on an ideal gas using the ideal gas law pV=nRT
    
    Parameters:
        number_of_moles (int): The number of moles of gas
        temperature (int): The temperature in Kelvin
        volume (float): The volume of the system in m^3
    Returns:
        float: The pressure of the system in Pa
      
    """
    if temperature < 0:
        raise ValueError('The temperature must be positive or zero')
    elif number_of_moles < 0:
        raise ValueError('The Number of moles must be positive')
    elif volume < 0:
        raise ValueError('The pressure must be positive')
    else:
        pressure = (number_of_moles* R * temperature)/(volume)
    return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Returns whether a specified transition is allowed or not
    
    Parameters:
        v_0(int):the original vibrational energy level
        v_1(int): the final vibrational energy level
    Returns:
        bool: A True or False value dictating whether a transition is allowed
    
    """
    Check = v_1 - v_0
    if isinstance(v_1, float) or isinstance(v_0, float):
        raise TypeError('The energy levels must be integer values')
    elif v_1 < 0:
        raise ValueError('The energy levels must be greater than or equal to zero')
    elif v_0 < 0:
        raise ValueError('The energy levels must be greater than or equal to zero')
    elif Check == 1:
        Check = True
    elif Check == -1:  
        Check = True
    else:
        Check = False
    
    return Check
     

# Function for coulomb
from scipy.constants import epsilon_0
from math import pi
def coulomb(r, q_i, q_j):
    """
    Returns either a value for potential energy or a list of potential energies for
    two charged particles at given values of r, seperation
    
    Parameters:
        r(int): The seperation of the two charged particles
        q_i(int): the charge of particle i
        q_j(int): the charge of particle j
    
    Returns:
    float or list: the potential energy between the two particles as either a float (if
    one value of r is given) or a list (if multiple values of r are given)
    
    """
    if isinstance(r, int):
        V = (q_i * q_j)/(4 * pi * epsilon_0 * r)
    else:
        V = []
        for i in r:
            V_r = (q_i * q_j)/(4 * pi * epsilon_0 * i)
            V.append(V_r)
    return V
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculates the goodness of fit of the model to the experimental data
    
    Parameters:
        model(array): The array of the values obtained by the model
        exp(array): The array of the values obtained experimentally
        exp_uncertainty(array): The uncertainity in the experimental values
        
    Returns:
        float: the goodness of fit value for the data
        
    """
    if len(model) != len(exp):
        raise ValueError('The lengths of the arrays must be the same')
    if len(exp) != len(exp_uncertainty):
        raise ValueError('The lengths of the arrays must be the same')
    for i in range(len(model)):
        for j in range(len(exp)):
            for k in range(len(exp_uncertainty)):
                if i != j:
                    continue
                if i != k:
                    continue
                else:
                    chi = np.sum((model[i] - exp[j])/exp_uncertainty[k])    
               
                print(chi)
                return chi


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates the rotational contribution to the molecular partition function for a molecule
    
    Parameters:
        N(int): the number of energy levels in the molecule
        rotational_constant(float): the rotational constant(B) for the molecule (in cm-1)
        temperature(int): the temperature of the molecuel (in K)
        
    Returns:
        float: The Rotational contribution to the molecular partition function
    """
    #converting rotational constant to m^-1
    B_m = rotational_constant*10
    if rotational_constant < 0:
        raise ValueError('The rotational constant must be a positive value')
    if temperature < 0:
        raise ValueError('The temperature must be a positive value')
    if isinstance(N, float):
        raise TypeError('The value of N must be an integer')
    N = np.arange(0, N+1)
    for i in N:
        q_r = np.sum(((2 * i) + 1) * np.exp((-h * c * B_m * i * (i + 1)) /( k * temperature)))
    
    return q_r



