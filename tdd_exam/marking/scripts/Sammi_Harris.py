# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """Allows the pressure of an ideal gas to be calculated
    
    Args:
        number_of_moles(float): The moles of the ideal gas (mol)
        temperature (float): The temperature of the system (K)
        volume (float): The volume of the gas (m^3)
    Return:
        float: The pressure of the  ideal gas (Pa) will given
    """
    if (number_of_moles > 0):
        pass
    else:
        raise ValueError ("The number of moles is unphysical, please enter ",
                          "a postive number of moles")
    if (temperature > 0):
        pass
    else:
        raise ValueError ("The temperature is unphysical, please enter ",
                          "a value greater than 0 Kelvin")
    if ( volume < 0): 
        raise ValueError ("The volume is unphysical, please enter ",
                          "a value greater than 0 m^3")
    else:
        return (number_of_moles * R * temperature) / volume


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """ Determines whether a given transition between original and 
        final vibrational level is allowed or forbidden.
        
     Args:
         v_0 (int): The vibration energy level of the inital state
         v_1 (int): The vibrational energy level of the excited state
         
      Return:
          bool: A boolean statement which says whether the transition is possible
     """

    if (type(v_0) == int):
        pass
    else:
        raise TypeError("The energy level must be an integer")
    if (type(v_1) != int):
        raise TypeError("The energy level must be an integer")
    elif (v_0 < 0) or (v_1 < 0):
        raise ValueError("The initial and final energy level must be ",
                         "greater than or equal zero. Check back over the values")    
    if np.abs(v_0 - v_1) == 1:
        return True
    else:
        return False
    if np.abs(v_0 - v_1) > 1:
         return False

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """The potential energy between two particles will be calculated knowing 
       the distance between the atoms as well as their charge.
       
        Args:
            r (float): The distance between the atoms
            q_i (float): The charge of atom i (C)
            q_j (float): The charge of atom j (C)
            
         Return:
            float: The potenetial energy betwen the two atoms in Joules
      """
    
    return (int(q_i) * int(q_j)) / (4 * np.pi * epsilon_0 * int(r))
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """Allows the goodness-of-fit paramater (chi squared) to be calculated 
       to measure how useful the data set is compared with the model.
       
       Args:
           model (float) : The data set from a certain moldel
           exp (float): The data set from an a conducted experimenet
           exp_uncertainty (float): The uncertainty in the experimental data set
         
        Return:
            float: The chi squared value between the two data sets to determine 
                   how "good" the data fits in
        
            """
    if (len(exp) == len(model) ):
        pass
    elif (len(exp) < len(model)):
         raise ValueError ("The number of elements in the expeirment data set",
                           " is less than that of the model, please make sure",
                           " the data sets are the same length")
    elif (len(model) < len(exp)):
         raise ValueError ("The number of elements in the model data set",
                           " is less than that of the model, please make sure",
                           " the data sets are the same length")      
    else:  
      
        return np.sum((exp - model/ exp_uncertainty))**2


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """Allows the rotation contribution of the molecular parition
       function to be calculated.
       
       Args:
           N (int) : The number of rotational energy levels
           rotational_constant (float): The rotational constant for a given 
                                        molecule (cm^-1)                 
           temperaure (float): The temperature of the system (K)
       Return:
              float: The contribution of the rotational component in the total
                     molecular partition function
           
     """
    if (temperature > 0):
        pass
    else:
        raise ValueError ("The temperature is unphysical, please enter ",
                          "a value greater than 0 Kelvin")
    if (rotational_constant > 0):
        pass
    else:
        raise ValueError ("The temperature is unphysical, please enter ",
                          "a value greater than 0 Kelvin")
    if (type(N) == int):
        pass
    else:
        raise TypeError("The N value must be an integer")
    return np.sum((2* N)*np.exp((-h*c * rotational_constant * N (N + 1))/(k*temperature)))