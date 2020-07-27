# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    determines the pressure of a system, assuming the gas is ideal, 
    with the given n, T and V.
    
    paramters: 
    n = moles of gas
    T = temperature 
    V = volume
    """
    if number_of_moles <= 0:
        raise ValueError('number_of_moles must be greater than 0')
    
    if temperature <= 0:
        raise ValueError('T value must be greater than 0')
    
    if volume <=0:
        raise ValueError('volume must be greater than 0')
        
    return (number_of_moles*temperature*R)/volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    determines whether the transition is allowed or not with the
    given vibrational energies
    
    parameters: 
    v_0 (int) = the first vibrational energy level
    v_1 (int) = the second vibrational energy level
    """
    
    if not isinstance(v_0, int):
        raise TypeError('v_0 must be an integer')
        
    if not isinstance(v_1, int):
        raise TypeError('v_1 must be an integer')
    
    if v_0 < 0:
        raise ValueError('v_0 must be greater than or equal to 0')
    
    if v_1 < 0:
        raise ValueError('v_1 must be greater than or equal to 0')
    
    if (v_0 - v_1) == 1 or (v_0 - v_1) == -1:
        return True
    else: 
        return False
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    determines the potential energy between two particles with the 
    given separation, r, and the chardes, q_i and q_j
    
    parameters: 
    r (int) = the separation between the two charged particles 
    q_i (int) = the charge of particle i
    q_j (int) = the charge of particle j
    """
    for t in np.array([r]):
        return (q_i*q_j)/(4*epsilon_0*np.pi*t)
    
    if not isinstance(r, int):
        raise TypeError('r must be an integer')
    
    return (q_i*q_j)/(4*epsilon_0*np.pi*r)
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    determines chi_squared of a set of experimental data and the 
    output from a model
    
    paramters: 
    model, exp and exp_uncertainty are only arrays, and not single
        values
    """
    if (len(model) != len(exp) or len(model)!= len(exp_uncertainty)
        or len(exp_uncertainty) != len(exp)):
        raise ValueError(print('\nThe error has been raised because'
              ' one of the data sets do not have the same number of'
              ' data points as each other.'))
    
    return (np.sum((np.array(exp)-np.array(model))/
                  np.array(exp_uncertainty)**2))
    
            
# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    determines the rotational contribution to the total partition
    function from the first given energy levels, N
    
    Arguments:
    rotational_constant = B = has the units of cm-1
    temperature = has the units of K
    
    Parameters:
    c = must be in the units of cm/s
    h = units of Js
    k has units of J/K
    """
    
    if not isinstance(N, int):
        raise TypeError('N must be an integer')
        
    if temperature < 0:
        raise ValueError('T must be greater than or equal to 0')
    
    if rotational_constant < 0:
        raise ValueError('B must be greater or equal to than 0') 
    
    n = np.arange(N+1)
    speed = c*100
    return np.sum((2*n+1)*np.exp((-h*speed*rotational_constant*
                                      n*(n+1))/(k*temperature)))