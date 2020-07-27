# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """ 
    Calculates the pressure occupied by an ideal gas
    
    Parameters:
        number_of_moles (float): Number of moles of the ideal gas.
        temperature (float): Temperature of the ideal gas (k).
        volume (float): Volume of ideal gas (m^3).
        
    Returns:
        float:Gas pressure (Pa) 
        
        """
    if temperature <0:
        raise ValueError ("The temperature is an unphysical value of <0.")
    if number_of_moles <0:
        raise ValueError("The number of moles is an unphysical value of <0")
    if volume <0:
        raise ValueError("The volume is an unphysical value of <0")
    return number_of_moles * R * temperature / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determines whether a transition between two energy levels
    is allowed.
    
    Parameters:
        v_0 (int): The initial vibrational energy level
        v_1 (int): The final vibrational energy level
        
    Returns:
        Boolean: True or False whether or not the transitions are allowed.
        
    """
    if v_0 < 0:
        raise ValueError("v_0 must be a integer greater or equal to 0")
    if v_1 <0:
        raise ValueError("v_1 must be a integer greater or equal to 0")
    if not isinstance(v_0, int):
        raise TypeError("v_0 must be an integer")
    if not isinstance (v_1, int):
        raise TypeError("v_1 must be an integer")
    
    return   -1<= v_1-v_0 <=1  
    
        
    
    
     

# Function for coulomb
from scipy.constants import epsilon_0
E_0 = float(epsilon_0)
def coulomb(r, q_i, q_j):
    """
    Calculates the potential energy between two
    charged particles for given separation and charges
    
    Parameters:
        r (can be array_like, int): Separation between two charged particles (nm)
        q_i(int) : Charge of first particle
        q_j (int): Charge of second particle
        
    returns:
        Array like, float:potential energies of charged particles (joules)
    """
    
    v = (q_i * q_j) / (4 * np.pi * E_0 * r)
    return v
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Determines chi squared (goodness of fit) between
    an experimental data set and model data set
    
    Parameters:
        model(array_like, float):model data
        exp(array_like, float):experimental data
        exp_uncertainty(array_like, float) : the uncertainty in the experimental data
          
    returns:
        float: the value of chi-squared
                goodness of fit
    """
    chi = np.sum(np.square((
        model - exp) / exp_uncertainty))
    return chi


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculates the rotational contribution to 
    the total partition function from the first N energy levels
    
    Parameters:
        N (int) : The number of energy levels
        rotational_constant(float): The rotational constant of the molecule (cm-1)
        temperature (float): The temperature of the molecule (K)
        
    returns:
        float: The rotational contribution of a given molecule (m)
    """
    if temperature <0:
        raise ValueError ("The temperature is an unphysical value of <0.")
    if rotational_constant <0:
        raise ValueError ("The rotational consttant is an unphysical value of <0.")
    if not isinstance(N, int):
        raise TypeError("N must be an integer")
   
     
    return np.sum((2*N +1) * np.exp((-h*c*rotational_constant 
                                     * N *(N+1))/ (k * temperature)))