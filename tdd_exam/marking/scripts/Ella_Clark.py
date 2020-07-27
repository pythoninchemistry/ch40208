# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the volume of a system given the variables in the ideal gas law
    
    Args:
        temperature(float): The temperature in Kelvin
        volume(float): The volume in m^3, must be physical value NOT less than 0 m^3
        number of moles (float): The number of moles in mol, should be physical value NOT less than 0 mol
   
    Returns:
        float: the pressure of the system in Pa 
    """
    if temperature<0:
        raise ValueError ("Temp must be physical amount eg. not less than 0")
    if number_of_moles<0:
        raise ValueError ("number of moles must be physical amount eg. not less than 0")
    if volume<0:
        raise ValueError ("volume be physical amount eg. not less than 0")
    else:
        return (number_of_moles * temperature * R)/volume



# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Returns True if transition between two vibrartional energy states is allowed and returns False if not.
    
    Args:
        v_0(int): The lower vibrational energy state, must be an integer greater than or equal to 0
        v_1(int): The higher vibrational energy state, must be an integer greater than or equal to 0
        
    Returns:
        Boolean:True if transition between two vibrartional energy states is allowed and returns False if not.
        
    """
    
    if not isinstance (v_0, int):
        raise TypeError ("v_0 must be an integer")
    if not isinstance (v_1, int):
        raise TypeError ("v_1 must be an integer")
    if v_0 <= 0:
        raise ValueError ("v_0 cannot be equal to or less than 0")
    if v_1 <= 0:
        raise ValueError ("v_1 cannot be equal to or less than 0")
    else:
        delta_v = v_0 - v_1
        if delta_v == 1:
            return(True)
        if delta_v == -1:
            return(True)
        else:
            return(False)
        
   
     

# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    """
    Returns the potential energy between two charged particles at a seperation, r
    
    Args:
        r(float): distance between two charged particles in Amstrongs
        q_i(int) = charge on particle i
        q_j(int) = charge on particle j
        
    Returns:
       float: Potential Energy between two charged particles i and j.

    
    """
    r = np.array(r)
    V = (q_i * q_j)/(4 * pi * epsilon_0 * r)
    return(V)
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Finds goodness of fit(Chi Squared)
    
    Args:
       model(float)(np array): model data
       exp(float)(np array): experimental data
       exp_uncertainty(float)(np array): The experimental uncertainty in the measurement 
       
    Returns:
        float: Chi Squared
   
    """
    if len(model) != len(exp):
        raise ValueError ("must have same amount of data points to compare")
    if len(exp_uncertainty) != len(exp):
        raise ValueError ("must have same amount of data points to compare")
    if len(model) != len(exp_uncertainty):
        raise ValueError ("must have same amount of data points to compare")
    else:
        chi_squared = np.sum(((exp - model)/exp_uncertainty)**2)  
    return(chi_squared)


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    
    """
    Finds the rotational contribution to the molecular partition function
    
    Args:
       N(int): Number of energy levels
       rotational_constant(float): The rotational constant in cm^(-1)
       temperature(float): The temperature in Kelvin (must not be less than 0) 
       
    Returns:
        float: Chi Squared
   
    """
    
    if not isinstance (N, int):
        raise TypeError ("N must be an integer")
    if temperature < 0:
        raise ValueError ("Temp must be physical amount eg. not less than 0")
    if rotational_constant <= 0:
        raise ValueError ("The rotational constant cannot be less than 0")
    else:
        l = []
        n = 0
        while len(l) <=N:
            l.append(n)
            n +=1
        for i in range (0, len(l)):
            q = np.sum(((2*i)+1) * np.exp(-((h * c * rotational_constant * i * (i + 1))/(k *temperature))))
        return(q)
     
 

    
  