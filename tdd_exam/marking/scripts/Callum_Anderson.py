# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Calculate the pressure of an ideal gas in this system (Pa)
    
    Args:
        number_of_moles (int): Number of moles in the system (mol)
        temperature (flaot): Tempereature of the system (K)
        volume (float): Volume of the system (m^3)

    Returns:
        float: Pressure of an ideal gas (Pa)
    """
#Errors to be raised
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    elif number_of_moles < 0:
        raise ValueError("The number_of_moles is unphysical (N < 0).")
    elif volume < 0:
        raise ValueError("The volume is unphysical (V < 0).")
#Value to be returned
    return ((number_of_moles*temperature*R)/volume)




# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determine if a vibrational transition is allowed according to vibrational
    selection rules
    
    Args:
        v_0 (int): First virbrational energy level
        v_1 (int): Second vibrational energy level

    Returns:
        Boolean (True/False): Statement for if the  vibrational transition is 
        allowed or not
    """ 
#Errors to be raised
    if v_0 <= 0:
        raise ValueError("The first energy level must be greater than 0.")
    elif v_1 <= 0:
        raise ValueError("The second energy level must be greater than 0.")
    elif not isinstance(v_0, int):
        raise TypeError("The first energy level must be an integer")
    elif not isinstance(v_1, int):
        raise TypeError("The second energy level must be an integer")
#Values to be returned
    elif  v_0 - v_1 == 1:
        return True
    elif v_0 - v_1 == -1: 
        return True
    else:
        return False

    
    
    
# Function for coulomb
from scipy.constants import epsilon_0
from scipy.constants import pi

def coulomb(r, q_i, q_j):
    """
    Calculate the potential energy between two charge particles at a certain seperation
    distance
    
    Args:
        r (int): Distance between the two charges
        q_i (int): Charge on the first particle 
        q_j (int): Charge on the second particle

    Returns:
        array_like, float: A list or array of the potential energies
    """ 
    
#Value for a single r
    if isinstance(r, int):
        return np.array((q_i*q_j)/((4*pi)*epsilon_0*r))
#Values for when there is multiple r
    else:
        r_list = []
        for i in r:
            r_Value = np.array((q_i*q_j)/((4*pi)*epsilon_0*i))
            r_list.append(r_Value)
        return r_list
    
    
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determine the goodness-of-fit parameter (x^2) for a set of data
    
    Args:
        model (array_like, floats): Set of experimental data
        exp (array_like, floats): Set of expected data
        exp_uncertainty (array_like, floats): Uncertainty in the experimental data  
    Returns:
        float: Goodness-of-fit parameter (x^2)
    """ 
#Errors to be raised
    if len(model) != len(exp) and len(exp_uncertainty):
        print("The data sets are not all the same length")
    elif len(exp) != len(model) and len(exp_uncertainty):
        print("The data sets are not all the same length")
    elif len(exp_uncertainty) != len(model) and len(exp):
        print("The data sets are not all the same length")
#Value to be returned
    return sum(((exp-model)/exp_uncertainty)**2)





#Function for partition

#Partially did this part!
    #All the errors raise correctly
    #Think rotational_contribution_Value is out by a long way off
        #Do get a list of values for list (0-N)
        #Could be a units issue
        #Could be the equation is inputted incorrectly
        #Could be that scipy.constant e is not math.exp
            #Cannot get math.exp to iterate over a list
    #rotational_contribution Needs to be 7 DP's
            
from scipy.constants import h, c, k, e

def partition(N, rotational_constant, temperature):
    """
    Calculate the rotational contribution to the molecular partition function
    
    Args:
        N (int): Number of energy levels being investigated
        rotational_constant (float): Rotational constant of the molecule (cm^-1)
        temperature (flaot): Tempereature of the system (K)      
    Returns:
        float: Rotational contribution to the molecular partition function 
    """
#Errors to be raised
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    elif rotational_constant < 0:
        raise ValueError("The rotational_constant is unphysical (B < 0).")
    elif not isinstance(N, int):
        raise TypeError("The number of energy levels must be an integer")
#Convert rotational_constant to m^-3
    rotational_constant = rotational_constant*100
#Make a list from 0 to N  
    N_list = []
    total = 0
    for n in range (1,N+1):
        total = total + n
        N_list.append(n)
#Need to sum over a list of values before the value is then returned
    rotational_contribution = []
    for i in N_list:
        rotational_contribution_Value = ((2*(i+1))*(e*(((-h*c*rotational_constant*i*(i+1))/(k*temperature)))))
        rotational_contribution.append(rotational_contribution_Value)
    return sum(rotational_contribution)