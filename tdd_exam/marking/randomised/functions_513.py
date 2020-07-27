# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):

    """
    Determines the pressure of a given number of gas molecules as a given temperature and volume
    after checking whether the temperature, number of moles and volume are allowed values.
    
    Parameters:
        number_of_moles (float): The number of moles of gas molecules. Must be >0.
        temperature (float): The temperature in Kelvin, must be > 0K.
        volume (float): The volume in cm^3. Must be > 0m^3
       
    Returns:
        float: The pressure of the gas in Pa.
    """
    if temperature<=0:
        raise ValueError('the temperature must be '
                         'greater than 0K.')
    elif number_of_moles<=0:
        raise ValueError('the number of moles must be '
                         'greater than 0.')
    elif volume<=0:
        raise ValueError('the volume must be greater '
                         'than 0m^3.')
    else:
        return (number_of_moles * temperature * R)/volume
    

# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    
    """
    Determines whether a transition is allowed for vibration spectroscopy.
    
    Parameters:
        v_0 (int): The original vibrational energy level. Must be a positive integer
        v_1 (int): The energy level after transition. Must be a positive integer, and
                   within +/- 1 of v_0
       
    Returns:
        Boolean: Whether the transition is allowed or not, as True/False.
    """
    
    if not isinstance(v_0,int) and not isinstance(v_1, int):
        raise TypeError('the vibrational energy '
                        'levels must be an integer.')
                
    elif not isinstance(v_0,int):
        raise TypeError('the original vibrational energy '
                        'level must be an integer.')
        
    elif not isinstance(v_1,int):
        raise TypeError('the final vibrational energy '
                        'level must be an integer.')
                
    elif v_0<=0 and v_1<=0:
        raise ValueError('the  vibrational energy '
                         'levels must be greater than 0.')
        
    elif v_0<=0:
        raise ValueError('the original vibrational energy '
                         'level must be greater than 0.')
        
    elif v_1<=0:
        raise ValueError('the final vibrational energy '
                         'level must be greater than 0.')
    
    elif v_1 < v_0 -1 or v_1 > v_0 +1:
            return False
    else:    
        return True
     

# Function for coulomb
from scipy.constants import epsilon_0
from math import pi

def coulomb(r, q_i, q_j):
    
    """
    Determines the potential energy between two charged particles at distance r,
    or at a set of distances given as a list.
    
    Parameters:
        r (float OR list): The distance between the two particles.
        temperature (float): The charge on one particle.
        volume (float): The charge on the other particle.
       
    Returns:
        float: The potential energy between the particles.
    """
   
    if isinstance(r,list):
        results = []
        for x in r:
            results.append ((q_i * q_j) / (4 * 3.141592653589793 * 8.854187817620389e-12 * x))
        return results
    else: 
        return (q_i * q_j) / (4 * 3.141592653589793 * 8.854187817620389e-12 * r)
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    
    """
    Determines the Chi squared value for a set of data, after checking that
    all data has been provied, i.e. the lengths of all fields are equal.
    
    Parameters:
        model (list): The ideal data points.
        exp (list): The experimental data points.
        exp_uncertainty (list): The uncertainty in each data point.
       
    Returns:
        float: The Chi^2 value of the data set compared to the model data.
    """
    
    if len(model)<len(exp):
        raise ValueError('model has too few values')
        
    elif len(model)<len(exp_uncertainty):
        raise ValueError('model has too few values')
        
    elif len(exp)<len(model):
        raise ValueError('exp has too few values')    
        
    elif len(exp)<len(exp_uncertainty):
        raise ValueError('model has too few values')

    elif len(exp_uncertainty)<len(model):
        raise ValueError('exp_uncertainty has too few values')    
        
    elif len(exp_uncertainty)<len(exp):
        raise ValueError('exp_uncertainty has too few values')  
    
    else:
        total = 0
        for x in range (len(exp)):
            chi = (((exp[x]-model[x])/exp_uncertainty[x])**2) 
            total = total + chi
        return total
   


# Function for partition
from scipy.constants import h, c, k
from math import e

def partition(N, rotational_constant, temperature):
    
    if rotational_constant < 0:
        raise ValueError('the rotational constant must be '
                         'greater than 0cm^-1.')
    elif temperature <= 0:
        raise ValueError('the rotational constant must be '
                         'greater than 0K.')
    elif not isinstance(N,int):
        raise TypeError('N must be an integer.')
    
    else:
        Qr = 0
        for n in range (N+1):
            x = (2*n+1)*(e**((-h*c*rotational_constant*n*(n+1))/(k*temperature)))
            Qr = Qr + x
        return Qr