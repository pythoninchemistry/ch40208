# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the volume occupied by an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        volume (float): Gas volume occupied (m^3).
    
    Returns:
        float: pressure of gas (Pa).
    """
    pressure = (number_of_moles*R*temperature)/volume
    
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0 K).")
    if number_of_moles < 0:
        raise ValueError("The number of moles of gas is unphysical (n < 0 mol).")
    if pressure < 0:
        raise ValueError("The pressure is unphysical (p < 0 Pa).")
    return  (number_of_moles*R*temperature)/volume
    
 


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """ 
    Determining whether a transition is allowed or not.
    
    Args:
      Original vibrational energy level  (v_0)
      Final vibrational energy level (v_1)
      
    Returns: 
      Boolean Variable
    """
    boolean = v_1 - v_0 
    
    if v_0 < 0:
        raise ValueError("The value of the original energy level is not equal to or greater than 0")
    if v_1 < 0:
        raise ValueError("The value of the final energy level is not equal to or greater than 0")
    if boolean > 1:
        return False
    if boolean < -1:
        return False
    if boolean == 0:
        return False
    if boolean == 1:
        return True
    if boolean == -1:
        return True
    if boolean == float:
        return False
    
  
    return boolean 
   
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Calculating the potential energy between two particles
    
    Args:
       Charge separation distances (r) (array_like, float)
       Charge of one particles (q_i)
       Charge of the other particle (q_j) 
       
    Returns:
       array_like, float: Energies for each of the distances 
    """ 
    
    return np.array((q_i*q_j)/ (4*np.pi*epsilon_0*np.array(r)))
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """ 
    Determining the χ2 of a set of experimental data and the output from a mode
    
    Args:
       Model data points (model)
       Experimental data points (exp) 
       The uncertainty in the experimental data points (exp_uncertainty)
    
    Returns: 
       Chi squared - gooodness of fit parameter
    """ 
    chi = np.sum((exp - model)/exp_uncertainty)**2
    
    return np.array(chi)


# Function for partition
from scipy.constants import h, c, k
                  
def partition(N, rotational_constant, temperature):
    """ 
    Finds the  rotational contribution to the total partition function#
    from the first 𝑁 energy levels
    
    Args: 
       J is the energy level, 
       h is the Planck constant, 
       c is the speed of light, 
       B is the rotational constant for the molecule, 
       k is the Boltzmann constant
       T is the temperature 
    Returns:
       qr which is the rotational contribution
    """
    Appropriate errors should be returned for a non-integer 

    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0 K).")
    if rotational_constant < 0:
        raise ValueError("The rotational_constant is unphysical (B < 0 ).")
    
    for J in range(0,N):
        contribution = np.sum((2*J + 1)*( np.exp((h*c*rotational_constant*J*(J+1))/k*temperature)))
    return contribution 



