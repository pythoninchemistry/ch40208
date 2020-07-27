# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    
    """
    For an ideal gas, will calculate the volume of a system
    
    Args:
        number_of_moles (float) = number of moles of the gas
        temperature (float) = temperature (K) of the gas
        volume = volume (m^3) occupied by the gas
        
    Returns:
        Volume (float) in m^3
    
    """
        
    if temperature < 0:
        raise ValueError ('Temperature in Kelvin must be greater than absolute zero')
    
    if number_of_moles < 0:
        raise ValueError ('The number of moles must be greater than zero')
    
    if volume < 0:
        raise ValueError ('The volume of gas must be greater than zero')
    
    else:
        return number_of_moles * R * temperature / volume

   

# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    
    """
    Function determining whether the transistion between two vibrational energy levels is allowed or not
    
    Args:
        v_0 (int): Initial vibrational energy level
        v_1 (int): Final vibrational energy level
    
    Returns:
        Boolean value (True if transition is allowed, False if transition is not allowed)
    
    """
   
    trans = v_1 - v_0
    
    
    if trans ==1:
        return True
    if trans == -1:
        return True
    
    if v_0 < 0: 
        raise ValueError ('Vibrational energy levels cannot be negative')
        
    if v_1 < 0:
        raise ValueError ('Vibrational energy levels cannot be negative')
    
    if not isinstance (v_0, int):
        raise TypeError ('Vibrational energy levels must be integers')
    
    if not isinstance (v_1,int):
        raise TypeError ('Vibrational energy levels must be integers')
   
   
    else:
        return False
    
   

    
    
    
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Finds the potential energy between two charged particles at different distances
    
    Args:
        r (array_like): seperation between particles (Angstroms)
        q_i (int) and q_j (int): charges of the two particles respectively (Coulombs)
        
    Returns:
        Potential energy of the two particles at the specified distances (array_like if r is a list, float if not)
        
    """
    numerator = q_i * q_j
    const = 4 * np.pi * epsilon_0
    
    if isinstance(r, int):
  
        potential_energy = numerator/(const * r)
        return potential_energy
    
    else:
        num_array = np.array([numerator, numerator])
        const_array = np.array([const, const])
        r_array = np.array([r])        
        potential_energy = num_array/(const_array * r_array)
    
        return potential_energy
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    
    """
    Chi_sqrd is the goodness of fit metric
    we want this as close to zero as possible so that the model fits the data well
    
    args:
        model (array_like) = model data
        exp (array_like) = experimental data
        exp_uncertainty (array_like) = the uncertainity in tthe data
        
    returns:
        the chi squared value, how close the model fits the data set

    
    """
  
    chi_sqrd = np.sum((model - exp)/(np.square(exp_uncertainty)))
    
    return chi_sqrd
    

    
     


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    
    """
    calculates the rotational contribution to the molecular partition coefficient 
    for N number of energy levels
    
    Args:
       N (int) = number of rotational energy levels for calculation
       rotational_constant (float) = rotational constant for the molecule (cm^-1)
       temperature (float) = temperature of system (K)
        
    returns:
        q_R (float) = rotational contribution to the molecular partition coefficient
    
    """
    
    if rotational_constant < 0:
        raise ValueError ('Rotational constant must be positive')
    
    if temperature < 0:
        raise ValueError ('Tempearture in Kelvin must be greater than zero')
        
    if not isinstance (N, int):
        raise TypeError ('Rotational energy levels must be integers')
    
    else:

        for i in np.arange (0, N):
            individual_q_R = ((2*i) +1) * (np.exp((-h * c * rotational_constant * i * (i+1))/(k * temperature)))
    
        q_R = np.sum(individual_q_R)
    
    return q_R