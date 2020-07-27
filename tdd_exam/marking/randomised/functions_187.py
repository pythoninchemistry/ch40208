# Import numpy
import numpy as np

# Function for ideal_gas_law
from scipy.constants import R

def ideal_gas_law(n, T, V):
    """
    Calculation of the pressure of a gas system for an ideal gas
    
    Args:
        n (float): number of moles of gas in system (mol)
        T (float): temperature of system (K)
        V (float): volume of gas in system (m^3)
        
    Returns:
        p (float): pressure of system (Pa)
    """
    
    if T <= 0:
        raise ValueError('Unphysical temperature given (T < 0K)')
    
    if n <= 0:
        raise ValueError('Unphysical number of moles given (n < 0)')
    
    if V <= 0:
        raise ValueError('Unphysical volume given (V < 0 m^3)')
    
    p = (n * R * T) / V
    
    return p


# Function for vib_spec_transition
def vib_spec_transition(v_0, v_1):
    """
    Determination of whether transition between two quantum states is allowed,
    dependent upon the vibrational spectroscopy selection rule.
    
    Args:
        v_0 (int): initial vibrational energy level before transition
        v_1 (int): final vibrational energy level after transition
        
    Returns:
        delta_v (Boolean): allowed (True) or disallowed (False) transition
    """
    
    delta_v = v_1 - v_0
    
    if delta_v == -1:
        delta_v = True
    elif delta_v == 1:
        delta_v = True
    else:
        delta_v = False
    
    if not isinstance(v_0, int):
        raise TypeError('v_0 must be integer')
    
    if not isinstance(v_1, int):
        raise TypeError('v_1 must be integer')
    
    if v_0 <= 0:
        raise ValueError('v_0 must be greater than 0')
    elif v_1 <= 0:
        raise ValueError('v_1 must be greater than 0')
    
    return delta_v
     

# Function for coulomb
from scipy.constants import epsilon_0

def coulomb(r, q_i, q_j):
    """
    Calculation of potential energy between two charged particles, dependent
    upon their separation
    
    Args:
        r (array_like, int): separation between charged particles (m)
        q_i (float): relative charge on particle i
        q_j (float): relative charge on particle j
        
    Returns:
        V_r (array_like, float): potential energy (eV)
    """
    if isinstance(r, int):
        V_r = (q_i * q_j) / (4.0 * np.pi * epsilon_0 * r)

    if not isinstance(r, int):
        V_r = []
        for i in range(0, len(r)):
            V = (q_i * q_j) / (4.0 * np.pi * epsilon_0 * r[i])
            V_r.append(V)
    
    return V_r
        
    
    

# Function for chi_squared
def chi_squared(model, exp, exp_uncertainty):
    """
    Calculation of the goodness of fit, chi-squared, between experimental and model data
    
    Args:
        model (array_like, float): model data
        exp (array_like, float): experimental data
        exp_uncertainty (array_like, float): uncertainty in experimental data
    """
    
    chi = np.sum(((exp - model)/exp_uncertainty) ** 2)
    
    if len(model) != len(exp):
        raise ValueError('All data arrays must be of same length')
    elif len(model) != len(exp_uncertainty):
        raise valueError('All data arrays must be of same length')
    elif len(exp) != len(exp_uncertainty):
        raise ValueError('All data arrays must be of same length')

    return chi



# Function for partition
from scipy.constants import h, c, k

def partition(N, B, T):
    """
    Calculation of the rotational contribution to the molecular
    partition function, for N energy levels
    
    Args:
        N (int): number of energy levels summation is occurring over
        B (float): rotational constant (cm^-1)
        T (float): temperature (K)
    
    Returns:
        q_r (float): rotational contribution to molecular partition function
    """
    J = np.arange(0, N + 1)
    
    q = []
    
    for i in range(0, len(J)):
        q_1 = ((2 * J[i]) + 1) * np.exp((-h * c * B * 100 * J[i] * (J[i] + 1))/(k * T))
        q.append(q_1)

    q_r = np.sum(q)
    
    if B <= 0:
        raise ValueError('B is unphysical (B < 0)')
    
    if T < 0:
        raise ValueError('T is unphysical (T < 0)')
    
    if not isinstance (N, int):
        raise TypeError('N must be an integer')

    return q_r
























