# Function for test 1
from scipy.constants import c, h

def energy(wavenumber):
    """
    Calculate the energy of a photon with a particular wavenumber
    
    Args:
        wavenumber (float): Photon wavenumber (m^-1).

    Returns:
        float: Photon energy (J).
    """
    return h * c * wavenumber


# Function for test 2
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, pressure):
    """
    Determine the volume occupied by an ideal gas.
    
    Args:
        number_of_moles (float): Number of moles of ideal gas.
        temperature (float): Gas temperature (K).
        pressure (float): Gas pressure (Pa).
    
    Returns:
        float: volume occupied (m^3).
    """
    if temperature < 0:
        raise ValueError("The temperature is unphysical (T < 0).")
    return number_of_moles * R * temperature / pressure


# Function for test 3
import numpy as np

def allowed_angular_momentum_quantum_numbers(principal_quantum_number):
    """
    Find the allowed angular momentum quantum numbers.
    
    Args:
        principal_quantum_number (int): Principal quantum number.
        
    Returns:
        array_like, int: A list or array of the allowed angular
                         momentum quantum numbers.
    """
    if principal_quantum_number <= 0:
        raise ValueError("The principal quantum number must be greater than 0.")
    if not isinstance(principal_quantum_number, int):
        raise TypeError("The principal quantum number must be an integer")
    return np.arange(0, principal_quantum_number)


# Function for test 4

def arrhenius_equation(pre_exponential_factor, activation_energy, 
                       temperature):
    """
    Determine the rate constant using the Arrhenius relationship.
    
    Args: 
        pre_exponential_factor (float): The pre-exponential factor (s^-1).
        activation_energy (float): The reaction activation energy (Jmol^-1).
        temperature (float): Reaction temperature (K)
    
    Returns:
        float: Reaction rate constant (s^-1).
    """
    return pre_exponential_factor * np.exp(-activation_energy / (R * temperature))


# Function for test 5

def morse(dissociation_energy, r, r_e):
    """
    Find the energy from a Morse potential.
    
    Args: 
        dissociation_energy (float): Energy of bond dissociation (eV).
        r (array_like, float): Distances to evaluate the energy for (Å).
        r_e (float): Equilibrium bond distance (Å).
    
    Returns:
        array_like, float: Energies for each fo the distances (eV).
    """
    return dissociation_energy * (1.0 - np.exp(-(r - r_e))) ** 2