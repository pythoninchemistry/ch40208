# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates gas pressure using the ideal gas law
    
    Arguments:
        number_of_moles(float): number of moles of gas
        temperature(float): temperature in Kelvin
        volume(float): volume of gas in m^3
        
    Returns:
        pressure(float): calculated pressure value
    """
    
    #calculation
    
    pressure = (number_of_moles*R*temperature)/volume
    
    #checks values are physical before returning result
    
    if temperature < 0:
        raise ValueError('Temperature given is less than 0K so is unphysical')
    
    elif number_of_moles < 0:
        raise ValueError('Number of moles given is less than 0 so is unphysical')
        
    elif volume < 0:
        raise ValueError('Volume given is less than 0 so is unphysical')
        
    else:
        return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether or not a transition is allowed between two given vibrational energy levels
    
    Arguments:
        v_0(integer): original vibrational energy level
        v_1(integer): final vibrational energy level
        
    Returns:
        transition(boolean): True if transition can take place, False if not
    """
    
    #calculates the delta v of transition
    
    delta = v_1 - v_0
    mod_delta = np.sqrt(delta*delta)
    
    if mod_delta == 1:
        transition = True
    else:
        transition = False
   
    #raises errors if needed
    
    if not isinstance(v_0, int):
        raise TypeError('Only integer energy level values are allowed')
    elif not isinstance(v_1, int):
        raise TypeError('Only integer energy level values are allowed')
    elif v_0 < 0:
        raise ValueError('Energy level value cannot be less than 0')
    elif v_1 < 0:
        raise ValueError('Energy level value cannot be less than 0')
    else:
        return transition
     

# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    """
    Calculates Coulomb potential between two charges separated by distance r, for both single values and arrays of r
    
    Arguments:
        r(int or float): distance between charges
        q_i(float): charge on first particle
        q_j(float): charge on second particle
    
    Returns:
        potential(float): electronic potential between charges
    """
    #calculates potential for single r value
    
    if isinstance(r, int):
        
        potential = (q_i*q_j)/(4.0*pi*epsilon_0*r)

    #calculates potential for array of values
    
    else:
    
        length = len(r)

        potential = np.zeros([length])

        i = 0

        while i < length:
            potential[i] = (q_i*q_j)/(4.0*pi*epsilon_0*r[i])
            i = i + 1
    
    return potential
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculates the chi squared value given a range of model values, experimental values and uncertainty values in each measurement
    
    Arguments:
        model(float): array of model values
        exp(float): array of experimental values
        exp_uncertainty(float): array of uncertainity values in each measurement
        
    Returns:
        chi_sq(float): the calculated chi squared value
    """
    #gets lengths of arrays
    
    length_m = len(model)
    length_e = len(exp)
    length_u = len(exp_uncertainty)
    
    #checks arrays are of equal length and performs calculation
    
    if length_m == length_e and length_e == length_u:
       
        i = 0
        chi_sq = 0
            
        while i < length_m:
            val = np.square((model[i] - exp[i])/exp_uncertainty[i])
            chi_sq = chi_sq + val
            i = i + 1

        return chi_sq
        
    else:
        raise ValueError('Arrays are not all of the same length')


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates the rotational contribution to the molecular partition function
    
    Arguments:
        N(int): number of rotational energy levels over which to sum
        rotational_constant(float): rotational constant for the molecule in cm^-1
        temperature(float): temperature of system
        
    Returns:
        rot_part(float): rotation contribution to partition function
    """
    
    #checks all values are physical and raises errors if not
    
    if rotational_constant < 0:
        raise ValueError('Cannot have a negative rotational constant')
    elif temperature < 0:
        raise ValueError('Cannot have a negative temperature value')
    elif not isinstance(N, int):
        raise TypeError('Only integer values of N are allowed')
    else:
        
        #converts B into SI units
        
        B = rotational_constant*100
        
        j = 0
        rot_part = 0
        
        while j <= N:
            
            exponent = ((-1*h*c*B*j*(j+1))/(k*temperature))
            preexponentialfactor = (2*j) + 1
            
            value = preexponentialfactor*np.exp(exponent)
            rot_part = rot_part + value
            
            j = j + 1
            
        return rot_part