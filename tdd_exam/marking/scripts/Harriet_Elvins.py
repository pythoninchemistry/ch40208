# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the pressure of an ideal gas using the ideal gas law: pV = nRT
    
    Parameters:
        number_of_moles (float): The number of moles of gas in the system (mol)
        temperature (float): The temperature of the gas in Kelvin (K)
        volume (float): The volume the ideal gas occupies (m3)
        
    Returns:
        pressure (float): The pressure of an ideal gas in Pascals (Pa)
    """
    if temperature <= 0: 
        raise ValueError('Unphysical temperature, temperature must be greater than 0')
    if number_of_moles <= 0: 
        raise ValueError('Unphysical number of moles, number of moles must be greater than 0')                  
    if volume <= 0:
        raise ValueError('Unphysical volume, volume must be greater than 0')
        
    else:
        pressure = (number_of_moles * R * temperature)/volume
        return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines if a vibrational transition obeys the selection rule where the 
    difference between the original and final vibration energy levels must be  
    plus or minus 1. If the difference is plus or minus 1, the transition is allowed,
    if the difference is a different value it is forbidden
    
    Parameters:
        v_0 (int): original vibrational energy level quantum number
        v_1 (int): final vibrational energy level quantum number
        
    Returns:
        decision (bool): Describes whether the transition is allowed or not, where 
        True refers to allowed transitions and False refers to forbidden transitions
    """
    if v_0 < 0 or v_1 < 0: 
        raise ValueError('vibrational energy levels must be greater than or equal to 0')
    if not isinstance (v_0, int):
        raise TypeError('vibrational energy levels are quantised so values must be intergers')
    if not isinstance (v_1, int):
        raise TypeError('vibrational energy levels are quantised so values must be intergers')
    
    else: 
        delta_v = v_0 - v_1
        if delta_v == 1 or delta_v == -1: # allowed transitions according to selection rules
            decision = True
        else: # all other values of delta_v are forbidden transitions.
            decision = False 
        return decision
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Calculates the potential energy (V(r)) between two charged particles at seperation (r) 
    using the coulomb potential equation
    
    Parameters:
    r (float or floats): The seperation distance between two charged particles i and j
    q_i (int): The charge of charged particle i
    q_j (int): The charge of charged particle j
    
    Returns:
    V_r (float or floats): The potential energy between 2 charged particles at seperation r
    """
    from math import pi
    
    r_new = np.array(r) 
    # if r is inputted as a list, this ensures the calculation occurs on each value of r in list.
    
    V_r= (q_i*q_j)/(4*pi*epsilon_0*r_new)
    
    return V_r



        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculates the goodness-of-fit parameter X_2, the sum of the squared difference 
    between experimental data and a model for data analysis
    
    Parameters:
        model (array): model data points
        exp (array): experimental data points
        exp_uncertainty (array): experimental uncertainty in the measurments of exp data points
        
    Return:
        X_2 (float): value of chi-squared from an experimental data set and a model.
    """
    len_model = len(model)
    len_exp = len(exp)
    len_exp_uncertainty = len(exp_uncertainty)
    
    if len_model != len_exp or len_exp != len_exp_uncertainty:
        raise ValueError('This error is caused by the arrays of data being different lengths.'
                         ' The experimental data cannot be compared to the model data if there' 
                         ' are unequal data points.')
    
    else: 
        X_2 = np.sum(np.square((exp - model)/exp_uncertainty))
        
        #The use of numpy means the calculation is carried out on all of the 
        #values in the arrays and these are then summed together to give one answer.
                
        return X_2
        



# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates the rotational contribution, q_r, of the molecular partition 
    function from the first N energy levels.
    
    Parameters:
    N (list): number of energy levels
    rotational_constant (float): The rotational constant of the molecule, in cm-1.
    temperature (float): The temperature in Kelvin, K.
    
    returns:
    q_r (float): The rotational contribution of the molecular partition function 
    for the first N energy levels
    
    """
    if not isinstance (N, int):
        raise TypeError('N must be an integer')
    elif rotational_constant < 0:
        raise ValueError('Unphysical rotational constant, the rotational constant '
                         'must be greater or equal to 0')
    elif temperature < 0:
        raise ValueError('Unphysical temperature, the temperature must be greater'
                         ' than or equal to 0')
        
    else:
        J = np.arange(0,N+1,1)  #creates list of the energy levels.
                                #N+1 ensures the array contains the value of N itself
        c_cm = c * 10 **2 #This ensures c is in the correct units of cm s-1       
        
        q_r = np.sum(((2*J)+1) * np.exp((-h*c_cm*rotational_constant*(J*(J+1)))/(k*temperature))) 
        
      
        #The use of numpy arrays means the calculation is carried out on all of the 
        #values in the array (the different energy levels) and these are then summed 
        #together to give one answer.
                
        return q_r


















