# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R #R = the gas constant

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculates the pressure of an ideal gas
    
    Parameters:
        number_of_moles(float): number of moles of gas present
        temperature(float): temperature in Kelvin, must be greater than zero
        volume(float): volume of container in mol dm-3
        
    Returns:
        Pressure(float): the corresponding pressure of the system in Pascales
    """
    if temperature < 0: #Ensuring the temperature is a real, positive value
        raise ValueError ('The temperature must be in Kelvin and greater than zero.')
    if volume < 0: #Ensuring the volume is a real, positive value
        raise ValueError ('The volume must be in mol dm-3 and greater than zero.')
    if number_of_moles < 0: #Ensuring the number of moles is a real, positive value
        raise ValueError ('The number of moles must be greater than zero.')
    return (number_of_moles*R*temperature)/volume #Calculating the pressure, in Pa


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether a vibrational energy transition is allowed or disallowed,
    based on the selection rule: delta_nu = +-1
    
    Parameters:
        v_0(int): The inital vibrational energy level
        v_1(int): The final vibrational energy level
       
    Returns:
        Boolean: True/false
    """
    if not isinstance(v_0, int): #Ensuring the initial frequency quantum number is an integar
        raise TypeError ('The frequency quantum numbers must be an integer')
    if not isinstance(v_1, int): #Ensuring the final frequency quantum number is an integar
        raise TypeError ('The frequency quantum numbers must be an integer')
    if v_0 < 0 or v_1 < 0: #Ensuring the frequency quantum numbers are both greater than zero
        raise ValueError ('The frequency quantum numbers must be greater than or equal to zero')
   
    #Determining if the difference in energy levels is allowed or disallowed
    if v_0 - v_1 == 1 or v_0 - v_1 == -1: 
        return True
    else:
        return False
    
     

# Function for coulomb
from scipy.constants import epsilon_0 #Epsilon_0 =  the permittivity of free space

def coulomb(r, q_i, q_j):
    """
    Calculates the coulomb potential between two particles, given their charge and distance
    
    Parameters:
        r(float/array): the distance between atom i and atom j
        q_i(int): the charge on atom i (in terms of electrons)
        q_j(int): the charge on atom j (in terms of electrons)
        
    Returns:
        float/array: the coulomb potantial between two atoms at input distance/distances
    """
    r = np.array([r]) #Forming a numpy array of r to use in calculations
    
    #Calculating the coulomb potential
    V = (q_i*q_j)/(4*np.pi*epsilon_0*r) 
    for i in range(len(V)):
        return V[i]   #Returning each value of the V array as individual values
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculates the chi squared value for a set of experimental data, given both the uncertainty and a model to compare against
    
    Parametrs:
        model(array): the theoretical data points
        exp(array): the experimental data points
        exp_uncertainty(array): the uncertainty in the experimental data
        
    Returns:
        chi_squared(float): the 'goodness of fit' of the experimental data compared to the theoretical
    """
    
    #Ensuring all the data is the same length
    if len(model) != len(exp): 
        raise ValueError ('The experimental and theoretical data must be the same length')
    if len(model) != len(exp_uncertainty):
        raise ValueError ('The theoretical and uncertainty data must be the same length')
    if len(exp) != len(exp_uncertainty):
        raise ValueError ('The experimental and uncertainty data must be the same length')
    
    return np.sum(((exp-model)/exp_uncertainty)**2) #Calculating chi squared


# Function for partition
from scipy.constants import h, c, k #h = Planck's constant; c = the speed of light; k = Boltzmann constant

def partition(N, rotational_constant, temperature):
    """
    Calculates the rotaional partition function of a molecule given the following parameters
    
    Parameters:
        N(int): the number of rotational energy levels present
        rotationl_constant(float): the rotational constant, B, for the molecule (in cm-1)
        temperature(float): the temperature, in Kelvin, of the molecule
        
    Returns:
        float: the rotational partition function of the molecule
    """
    if rotational_constant < 0: #Ensuring the rotational constant is positive
        raise ValueError ('The rotational constant must be positive')
    if temperature <= 0: #Ensuring the temperature is positive and in Kelvin
        raise ValueError ('The temperature must be in Klevin, and greater than zero')
    if not isinstance(N, int): #Ensuring N is an integar
        raise TypeError ('The value of N must be an integar')
    
    
    #Calculating the rotational partition function
    partition_functions = [] #Creating an empty list of partition funcitons to append to
    B = rotational_constant * 100 #Converting the rotational constant to SI units
    for i in range(N+1):    
        q = (2*i+1)*(np.exp((-h*c*B*i*(i+1))/(k*temperature)))
        partition_functions.append(q) #Appending each of the calculated partition function values (for each quantum level) to a list
        
    
    return np.sum(partition_functions) #Summing all calculated values of the partition function, at each quantum energy level,
                                       #to give the total rotational partition function for the molecule