# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    """
    Determine the pressure occupied by an ideal gas.
    
    Arguments:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        volume (float): Volume of gas (m^3).
    
    Returns:
        float: pressure of gas (Pa).
    """
    
    #converting the inputs into more managable letters
    n = number_of_moles
    T = temperature
    V = volume
    
    #raises error if T<0
    if T < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    
    #raises error is n < 0
    if n < 0:
        raise ValueError("The number of moles is unphysical (n < 0).")
    
    #raises error if V < 0
    if V < 0:
        raise ValueError("The volume is unphysical (V < 0).")
    return ((n*R*T)/V)


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determine whether a transition between two vibrational energy levels
    is allowed.
    
    Arguments:
        v_0 (int): Original energy level.
        v_1 (int): Final energy level.
    
    Returns:
        bool: Whether the transition is allowed (True) or not allowed (False).
    """
    
    #calculating transition
    transition = (v_1 - v_0)
    
    #raises ValueError if either vibrational energy level is less than 0
    if v_0 < 0 or v_1 < 0:
        raise ValueError("The vibrational energy levels"
                         "must be greater than or equal to 0.")
    
    #Raises TypeError if either energy level is not an integer
    if not isinstance(v_0, int) or not isinstance(v_1, int):
        raise TypeError("The vibrational energy levels must be integers")
    
    
    else:
        if transition == 1 or transition == -1 or transition == 0:
            return True
        else:
            return False

# Function for coulomb
from scipy.constants import epsilon_0
import numpy as np
from numpy import pi

def coulomb(r, q_i, q_j):
    """
    Calculates the potential energy between two charged particles.
    
    Arguments:
        r (either float or list/array): The distance between the two particles (m).
        q_i (int): Charge of particle i
        q_j (int): Charge of particle j
    
    Returns:
        float or array of floats: Potential energy
        (or energies if array/list of distances is used) between the two particles.
            
    """
    #Raises an error if more than one charge is given for either particle.
    if not isinstance(q_i, int) or not isinstance(q_j, int):
        raise TypeError("There should only be one charge input (integer)"
                        "for each particle.")
    
    distances = np.array([r])
    for r in distances:
        return ((q_i*q_j)/(4*np.pi*epsilon_0*r))
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculates goodness of fit between experimental data and the model.
    
    Arguments:
        model (float): The model data
        exp (float): The experimental data
        exp_uncertainty (float): the uncertainty in the experimental data.
    
    Returns:
        float: The goodness of fit of the data (Chi squared).
    """

    return np.sum(np.square((model - exp) / exp_uncertainty))


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    """
    Calculating the rotational contribution
    to the molecular partition function.
    
    Arguments:
        N (int): The maximum energy level calculated
        rotational_constant (float):  The rotational constant of the molecule (cm^-1).
        temperature (int): The system temperature (K).
        
    Returns:
        float: the rotational contribution to the molecular partition function.
   
    """
   
    #converting arguments to more managable letters
    #(also converting B to correct units (m^-1))
    B = rotational_constant*100
    T = temperature
    
    #Raises ValueError if T < 0
    if T < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
        
    #Raises ValueError if B < 0    
    if B < 0:
        raise ValueError("The rotational constant is unphysical (B < 0).")
    
    #Raises TypeError if N is not an integer
    if not isinstance(N, int):
        raise TypeError("N must be an integer")
    
    #creates array where each entry is one of the energy levels to be calculated,
    #up to N
    J_values = np.arange(0,N+1)
    
    q_R = 0
    

    """
    For each J value in the J_values array, the rotational contribution is calculated
    and added together with the other values to give q_R, the final value to be returned.
    """
    
    for J in J_values:
        
        q_R += (2*J+1)* np.exp((-h*c*B*J*(J+1))/(k*T))
    
    return q_R