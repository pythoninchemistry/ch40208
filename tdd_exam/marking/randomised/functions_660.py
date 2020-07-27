# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the pressure of an ideal
    gas with a known number of moles,
    temperature and volume. 
    
    Arguments:
    number_of_moles (int): the number of
    moles for the ideal gas (mol)
    temperature (int): the reaction 
    temperature (K)
    volume (float): the volume of the 
    ideal gas (dm^3)
    
    Returns: 
        float: the pressure of an 
        ideal gas
    """
    
    if temperature < 0: 
        raise ValueError('The temperature'
                         'must be above zero'
                         'degrees') 
    if number_of_moles < 0: 
        raise ValueError('the number of moles'
                         'must be greater than'
                         'zero')
    if volume < 0: 
        raise ValueError('the volume of an ideal'
                         'gas must be greater'
                         'than zero') 

    return (number_of_moles * R * temperature) / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Calculates the allowed transitions 
    between one quantum state and 
    another for vibrational 
    spectroscopy following the selection
    rule 
    
    Arguments: 
    v_0 (int): the original vibrational energy level
    v_1 (int): the final vibrational energy level 
    
    Returns: 
        (Bool): the allowed transitions 
        for vibrational spectroscopy
    """
    if v_0 < 0: 
        raise ValueError('The vibrational energy level'
                         'must be greater than zero') 
    if v_1 < 0: 
        raise ValueError('The vibrational energy level'
                         'must be greater than zero') 
    if not isinstance (v_0, int): 
        raise TypeError('The vibrational energy level'
                        'must be an integer')
    if not isinstance (v_1, int): 
        raise TypeError('The vibrational energy level'
                        'must be an integer')
    if not isinstance (v_0, int) and not isinstance (v_1, int): 
        raise TypeError('Both vibrational energy levels'
                        'must be integers')
    
   
    difference = v_1 - v_0
    
    if difference == 1:
        return True 
    elif difference == -1:
        return True 
    else: 
        return False 
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Calculates the potential energy between 
    two charged particles with given 
    seperation and charges
    
    Arguments: 
    r (array_like, int): the separation 
    between the two charged particles 
    q_i (int): the charge on the first particle 
    q_i (int): the charge on the second particle
    
    Returns: 
        (float): the potential energy of a
        charged particle 
    """
    
    if isinstance (r, int):
        return (q_i * q_j) / (4.0 * np.pi * epsilon_0 * r) 
    elif isinstance (r, list):
        r = np.array(r)
        return (q_i * q_j) / (4.0 * np.pi * epsilon_0 * r) 
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculates chi squared to determine 
    the goodness of fit between 
    experimental data and a model
    
    Arguments: 
    model(array_like, float): the model 
    data
    exp (array_like, float): the experimental
    data 
    exp_uncertainty (array_like, float): the
    uncertainty in the measurement of the 
    experimental data
    
    Returns:
        int: the chi squared value
    """
    model == np.array(model)
    exp == np.array(exp)
    exp_uncertainty == np.array(exp_uncertainty)
    chi = np.sum(((exp - model) / exp_uncertainty) ** 2 )
    
    if len(model) != 3:
        raise ValueError('the model array has'
                        'too few values')
    if len(exp) != 3: 
        raise ValueError('the exp array has'
                        'too few values')
    if len(exp_uncertainty) != 3: 
        raise ValueError('the exp_uncertainty array'
                        'has too few values')
    return chi


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates the rotational contribution 
    to the molecular partition function 
    
    Arguments: 
    N (int): the total number of energy levels
    rotational_constant (float): the rotational 
    constant for the molecule (cm-1)
    temperature(int): the temperature of the
    reaction (K)
    
    Returns:
        float: the rotational contribution to the 
        molecular partition function
    """
    if rotational_constant < 0: 
        raise ValueError('The rotational constant must be'
                         'greater than zero')
    if temperature < 0: 
        raise ValueError('The temperature must be greater'
                         'than zero')
    if not isinstance (N, int): 
        raise TypeError('the number of energy levels'
                        'must be an integer') 
         
    J = 0
    N = N
    n = 1
    q = np.sum(2*J + 1)* (np.exp((-h * c * rotational_constant * J * (J+1)) / (k * temperature)))
    
    energy_levels = range(0, N)
    for i in range(len(energy_levels)): 
        while i <= N:
            J = J + n 
            if energy_levels[i] > N: 
                   break 
    return q 

#trying to write a while loop to do the summation over the values J = 0 to J = N 
#and then use the equation given
   
        