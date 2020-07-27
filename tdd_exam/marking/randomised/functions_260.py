# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):

    '''
    Function:
        Calculates the pressure of an ideal gas from known values of: the number of moles of gas, temperature and volume.
        
    Arguments:
        number_of_moles (int) : The number of moles of gas present in the sample, must be greater than or equal to 0
        temperature (int) : The temperature of the sample in Kelvin, must be greater than or equal to 0
        volume (float) : The volume of the sample (unknown units, assume m^3), must be greater than or equal to 0
        
    Return:
        Returns the pressure in pascals.
    '''
    
    # Question says calculate volume but values given in test 1 are (number_of_moles, temperature, volume) and the target is a pressure #
    # Same as above for question 2, so I have made a function to calculate the pressure #
    
    # I assumed test 5 is looking for an unphysical volume, not pressure. As this is the last variable that needs to be checked #
    # I have written a statement that would check for an unphysical pressure though, see Extra Statemant 1 #
    
    # Tests for inappropriate values #
    
    if temperature < 0:
        raise ValueError
        
    if number_of_moles < 0:
        raise ValueError
        
    if volume < 0:
        raise ValueError
        
    # Extra Statement 1 : Checks for an unphysical pressure #
        
    if ((number_of_moles*R*temperature)/volume) < 0:
        raise ValueError
        
    # Equation for calculating the pressure of an ideal gas #    
    # Statement to return pressure value #
    
    else:
        pressure = (number_of_moles*R*temperature)/volume
        return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    
    '''
    Function:
        Calculates the change in quantumn number between two vibrational energy levels.
        
    Arguments:
        v_0 (int) : The initial energy levels quantum number
        v_1 (int) : The final energy levels quantum number
        
    Return:
        Returns the change in quantumn number between two vibrational energy levels.
    '''
    
    # Equation to calculate delta_v #
    
    delta_v = v_1 - v_0
    
    # Statement to check for correct value type #
    
    if type(v_0) != int or type(v_1) != int:
        raise TypeError
        
    # Statement to check for correct value sign for v_0 and v_1 #
        
    elif v_0 < 0 or v_1 < 0:
        raise ValueError
        
    # Statements to check if delta_v +/- 1 #
    
    elif -1 <= delta_v <= 1:
        return True
    
    elif delta_v < -1 or delta_v > 1:
        return False
    
    
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    
    '''
    Function:
        Calculates the potential energy between two charged particles at a single distance, or calculates a list of potential energies
        from a list of separations.
        
    Arguments:
        r (int) : The value of the separation (in m ?)
        q_i (int) : The charge on the first particle
        q_j (int) : The charge on the second particle

    Return:
        Returns the potential energy from a single r value, or a list of potential energies from a list of r values
    
    '''
    
    from math import pi
    
    # Equation for calculating potential energy os r is an integer #
    
    if type(r) == int:
        V_r = (q_i*q_j)/(4*pi*epsilon_0*r)
        return V_r
    
    # Equation for calculating the list of potential energy values from a list of r values #
    
    if type(r) == list:
        V_r_list = []
        for i in r:
            V_r_list.append((q_i*q_j)/(4*pi*epsilon_0*i))
        return V_r_list
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    
    '''
    Function:
        Calculates the chi squared value between an experimental data set including error, and a model.
        
    Arguments:
        model (np.array) : A numpy array containing values from the model
        exp (np.array) : A numpy array containing values from the experiment
        exp_uncertainty (np.array) : A numpy array containing the uncertainty values on the experimental data

    Return:
        Returns the value of chi squared
    
    '''
    
    # Error message prints if variables are not the same length #
        
    if len(model) != len(exp) or len(model) != len(exp_uncertainty) or len(exp) != len(exp_uncertainty):
        print('')
        print('ValueError : The variables are not of equal length, currently:')
        print('             model length           = {}'.format(len(model)))
        print('             exp length             = {}'.format(len(exp)))
        print('             exp_uncertainty length = {}'.format(len(exp_uncertainty)))
        raise ValueError
        
    # Equation for calculating chi_squared #
        
    else:
        chi_squared = np.sum(np.square((exp-model)/exp_uncertainty))
        return chi_squared


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    
    '''
    Function:
        Calculates the rotational contribution to the molecular partition function from all rotational energy levels from J = 0 
        to J = N (inclusive of J = N)
        
    Arguments:
        N (int) : Maximum J quantum number level to be summed over
        rotational_constant (float) : The value of the rotational constant, B, in cm^-1
        temperature (int) : The temperature in Kelvin
        
    Return:
        Returns the rotational contribution to the molecular partition function.
    
    '''
    
    from math import exp
    
    energy_level_array = []
    
    # Statements to check for approptiate values for rotational_constant, temperature and N #
    
    if rotational_constant < 0:
        raise ValueError
        
    elif temperature < 0:
        raise ValueError
        
    elif type(N) != int:
        raise TypeError
        
    # Calculates the energy of each J level, and appends it to an array. The value of c needs to be converted to cms-1#
    # The appended array is then summed after the for loop has finished #
        
    else:
        for i in range(0, N+1, 1):
            energy = ((2*i)+1)*exp((-h*(c*100)*rotational_constant*i*(i+1))/(k*temperature))
            energy_level_array.append(energy)

        energy_sum = np.sum(energy_level_array)

        return energy_sum











