import numpy as np
def calculate_gps_time_dilation(orbit_height, days):
    """
    Calculate combined relativistic effects on GPS satellites
    
    Parameters:
    orbit_height (float): Height of orbit in meters
    days (float): Number of days
    
    Returns:
    tuple: Special and general relativistic time differences
    """
    # Constants
    c = 299792458  # Speed of light (m/s)
    G = 6.67430e-11  # Gravitational constant
    M = 5.97e24  # Mass of Earth (kg)
    R = 6.37e6  # Radius of Earth (m)
    
    # Orbital velocity
    v = np.sqrt(G*M/(R + orbit_height))
    
    # Special relativistic time dilation
    special_dilation = days * 86400 * (1/np.sqrt(1-v**2/c**2) - 1)
    
    # General relativistic time dilation
    general_dilation = days * 86400 * (
        1/np.sqrt(1-2*G*M/(c**2*(R+orbit_height))) - 1
    )
    
    return special_dilation, general_dilation

# Example calculation for GPS satellite
orbit_height = 20200000  # 20,200 km
days = 1

special_effect, general_effect = calculate_gps_time_dilation(
    orbit_height, days
)

print(f"After {days} day:")
print(f"Special relativistic effect: {special_effect*1e9:.2f} ns")
print(f"General relativistic effect: {general_effect*1e9:.2f} ns")