# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    
    '''
    Function to determine the pressure of an ideal gas according
    to the ideal gas law, PV=nRT
    
    Arguments:
    number_of_moles (float) : Number of moles of gas 
    temperature (float): The temperature the gas is at in Kelvin
    volume (float) : The volume occupied by the gas in Pa
    
    Returns:
    float : The pressure
    
    '''

    if temperature < 0:
        raise ValueError('The temperature cannot be'
                         'less than 0K')
    if number_of_moles < 0:
        raise ValueError('The number of moles cannot be'
                         'less than 0')
    if volume < 0:
        raise ValueError('The volume cannot be less'
                         'than 0')
    
    return (number_of_moles*R*temperature)/volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    
    '''
    Function to determine whether a transition between two'
    vibrational energy levels is allowed or not
    
    Arguments:
    v_0 (int) : initial energy level
    v_1 (int) : final energy level
    
    Returns:
    Boolean : True if the transition is allowed and false
              if the transition is not allowed
              
    '''
  
    
    if v_0 < 0:
        raise ValueError('The vibrational energy level'
                         'v_0 cannot be less than 0')
    if v_1 < 0:
        raise ValueError('The vibrational energy level'
                         'v_1 cannot be less than 0')
    if not isinstance(v_0, int):
        raise TypeError('vibrational energy level v_0'
                        'must be an integer')
    if not isinstance(v_1, int):
        raise TypeError('vibrational energy level v_1'
                        'must be an integer')
    
    return v_1 == (v_0+1) or v_1 == (v_0-1)

    
      

        

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    
    '''
    Function to model the potential energy between two
    charged particles at a variable distance
    
    Arguments:
    r (float) : separation between the two charged particles
    q_i (int) : charge on first particle
    q_j (int) : charge on second particle
    
    Returns:
    float : V(r), the potential energy between the two particles
    
    '''
    
   
    return np.array((q_i*q_j)/((int(4))*(np.pi)*epsilon_0*(r)))
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    
    '''
    Function to determine the goodness of fit
    between experimental data and model data
    
    Arguments:
    model (array) : model data
    exp (array) : experimental data
    exp_uncertainty (array) : experimental uncertainty
                              in measurement of experimental
                              data
                              
    Returns:
    float : goodness of fit value for experimental data
            and model data
            
    '''
    
    return sum(np.array(((exp - model)/exp_uncertainty))**2)



# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    
    '''
    Function to return the rotational contribution to
    the molecular partition function
    
    Arguments:
    N (int) : The number of energy levels to be summated over
    rotational_constant (float) : The rotational constant
                                  for the molecule
    temperature (float) : the temperature
    
    Returns:
    float : the rotational contribution to the molecular
            partition function
            
    '''        
    
    
    if rotational_constant < 0:
        raise ValueError('Rotational Constant cannot'
                         'be a negative value')
    if temperature < 0:
        raise ValueError('Temperature cannot'
                         'be less than 0K')
    if not isinstance(N, int):
        raise TypeError('Value of energy level N'
                        'must be an integer')
       
    else:
        return sum(np.array(((2*N)+1)*(np.exp((-h*c*rotational_constant*N*(N+1))/k*temperature))))
    





















