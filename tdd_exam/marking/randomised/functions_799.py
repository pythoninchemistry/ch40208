# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, pressure):
    """
    Caculates the volume from an input no. of moles 
    ,temperature value and pressure value
    
    Args: 
        number_of_moles (float): the number of moles of gas
        temperature(float): temperature of system
        pressure(float): pressure of system
    
    Returns:
        (float)volume of gas
    """
    if number_of_moles < 0 or temperature < 0 or pressure < 0:
        raise ValueError ('values for number of moles, temperature and  pressure'
                          'that are less than zero are unphsical')
    
    else:
        return (number_of_moles * R * temperature) / (pressure)


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Asserts whether a vibrational transition between 2 input energy levels
    is allowed or not
    
    Args: 
        v_0 (int):  initial vibrational energy level
        v_1 (int):  final vibrational energy level
    
    Returns:
        (boole)judgement on whether the transition is allowed
    """
    
    test_array = np.array([v_0, v_1])
    
    if isinstance (v_0, float) or isinstance (v_1, float):
        raise TypeError ('values for v must be whole numbers')
    elif v_0 <= 0 or v_1 <= 0:
        raise ValueError ('values for v must be positive')
    elif (np.diff(test_array))**2 == 1:
        return True
    else:
        return False
        
# Function for coulomb
from scipy.constants import epsilon_0
    

def coulomb(r, q_i, q_j):
    """
    Calculates the potentual between two charged particles, 
    at a separation r, given the charges of both the particles
    
    Args: 
        r(float, array like) : seperation of the particles
        q_i (int) : charge of the first particle
        q_j (int) : charge of the second particle
    
    Returns:
        (float, array like) : value(s) for the potential energy
    """
    
    if isinstance (r, int):
        return (q_i * q_j)/(4 * np.pi * epsilon_0 * r)
    else:
        potential_energy = []
        
        for i in r:
            potential_energy.append((q_i * q_j)/(4 * np.pi * epsilon_0 * i))
        
        return potential_energy
    
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculates the chi squared paramiter for between given experimental data, 
    model data and the assosiated uncertainty
    
    Args: 
    model(array like) = model data set
    exp(array like) = experimental data set
    exp_uncertainty(array like) = uncertainty data set
    
    Returns:
        (array like) : Chi squared values data set
    """
    
    length_of_mod = len(model)
    length_of_exp = len(exp)
    length_of_exp_uncertainty = len(exp_uncertainty)
    
    
    if length_of_mod < (length_of_exp + length_of_exp_uncertainty)/2:
        raise ValueError ('model data has too few data points')
        
    elif length_of_exp < (length_of_mod + length_of_exp_uncertainty)/2:
        raise ValueError ('experimental data has too few data points')
        
    elif length_of_exp_uncertainty < (length_of_mod + length_of_exp)/2:
        raise ValueError ('experimental uncertainty data has too'
                          ' few data points')
        
    else:
        chi_squared_res = np.sum(np.square((
        model - exp) / exp_uncertainty))
        return chi_squared_res


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
       
    if rotational_constant < 0:
        raise ValueError('unphysical B')
    elif temperature < 0:
        raise ValueError('unphysical temperature')
    elif isinstance (N, int) == False:
        raise TypeError ('N must be a whole Number')
    else:
        J_values = np.arange(0, N + 1)
    
        individual_rotational_contribution = []
    
        for i in (J_values):
            individual_rotational_contribution.append(
            ((2*i) + 1) * np.exp((-h) * (c*(10**2)) * rotational_constant * i * (i + 1)/
                              (k * temperature)))
        final_value = np.array(individual_rotational_contribution)
        return np.sum(final_value)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        