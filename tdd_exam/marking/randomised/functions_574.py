# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, volume):
    '''
    this function calculates the pressure of an ideal gas 
    using the ideal gas law when passed the number of moles,
    temperature and the volume of the gas being observed.
    
    Args:
        number_of_moles (float): number of moles of ideal gas.
        temperature (float): temperature of the ideal gas .
        volume (float): volume of the ideal gas .
        
    Returns: 
        float: corresponding pressure of the ideal gas.
    '''
        
    if temperature < 0:
        raise ValueError('the input temperature is not a' 
                         ' physical temperature, input a'
                         ' temperature > 0K')
    elif number_of_moles < 0:
         raise ValueError('the input number of moles is'
                          ' not a physical amount, input a'
                          ' value > 0')
    elif volume < 0:
          raise ValueError('the input volume is not a'
                           ' physical ampunt, input a'
                           ' value > 0')
                         

    pressure = ((number_of_moles*R*temperature)
                           /volume)
    return pressure


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    '''
    determines if a vibrational engergy level transition is allowed
    according to the selection rule for vibrational spectroscopy.
    
    Args:
        v_0 (int) : inital vibrational energy level
        v_1 (int) : final vibrational energy level
    
    Returns:
        (bool) : statement determining if transition is allowed
    
    '''
    
    if v_0 < 0 or v_1 <0:
        raise ValueError ('vibrational energy levels cannot'
                          ' take a negative value,input value >= 0')
    if not isinstance (v_0, int):
        raise TypeError ('vibrational states are quantised so'
                         ' input values of  v_0 must be an integer')
        
    if not isinstance (v_1, int):
        raise TypeError ('vibrational states are quantised so'
                         ' input values of  v_1 must be an integer')
         
    
    difference  = v_1 - v_0
    
    if difference == 1 or difference == -1:
        decision = True
    elif difference != 1 or difference != -1:
        decision = False
     
    return decision
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    '''
    calculates the potential energy of two charged particles with a 
    separation distance of r and charges q_j and q_j
    
    Args: 
        r (array) : individual distance or aryyay of distances
        q_i (float): charge of molecule 1
        q_j (float): charge of molecule 2
        
    Returns:
        array: potential energy at corresponding distances r
    '''
    import numpy as np
    
    if isinstance (r, int):
        pot_E = ((q_i*q_j) /
                 (4*np.pi*epsilon_0*r))
        
    elif not isinstance (r,int):
        r = np.array(r)
        output = np.array([])
        for a in r:
            pot_E = ((q_i*q_j)/(4*np.pi*epsilon_0*a))
            np.append(output,pot_E)
        
    return output
        
    
# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    
    '''
    Calucalated chi squared value (how good is the fit?) for a model mixed
    IR spectrum vs an experimeantally generated IR spectrum.
    the fractional make up of the model must also be defined.
    
    Parameters: 
       
        model (numpy array): array of values from known dataset
        
       exp (numpy array): array of values from the experimental dataset
                                     
        Exp_uncertainty (numpy array): array of uncertainties for tranmisttance values 
                                                 from experimental dataset
    
    Returns: 
        array: Chi squared value for the modeled transmittance.
    '''
        
    import numpy as np
    M = len(model)
    E = len(exp)
    U = len(exp_uncertainty)
    if E != M or E != U:
        raise ValueError('the array of the experimental has different'
                         ' size to the other arrays, check size matches')
    elif M != E or M != U:
        raise ValueError('the array of the model has different'
                         ' size to the other arrays, check size matches')
    elif U != M or U != E:
        raise ValueError('the array of the experimental error has different'
                         ' size to the other arrays, check size matches')
    
    

    Chi_squared = np.sum(((exp-model)/exp_uncertainty)**2)
    
    return Chi_squared


# Function for partition
from scipy.constants import h, c, k

def partition(N, rotational_constant, temperature):
    '''
    calculates the rotational contribution to the molecular partition function over a
    range of rotational energy leves from J=0 tp J=N
    
    Args: 
        N(int): number of energy levels to sum over
        rotational_constant (float): rotational constant of the molecule in cm^-1
        Temperature (float): the temperature at which the observation is taking palve (K)
    
    returns:
        float; rotational partition function.
        
    '''
    import numpy as np 
    
    if rotational_constant < 0:
        raise ValueError('the rotational_constant is not a' 
                         ' physical rotational_constant, input a'
                         ' rotational_constant > 0')
    
    if temperature < 0:
        raise ValueError('the input temperature is not a' 
                         ' physical temperature, input a'
                         ' temperature > 0K')
    
    if not isinstance (N,int):
        raise TypeError ('roational states are quantised so'
                         ' input values of  the rotational constant'
                         ' munst be an interger')
    J = np.arange(0,N-1)
    
    for i in J:
        q_r = np.sum((2*i+1)*np.exp((-h*c*rotational_constant*i*(i+1))
                                    /(k*temperature)))
    return q_r
          
    
    