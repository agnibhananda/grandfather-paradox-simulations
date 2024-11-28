import numpy as np
import matplotlib.pyplot as plt

def simulate_twin_paradox(
    velocity_outbound,
    velocity_return,
    journey_time_earth
):
    """
    Simulate the Twin Paradox
    Parameters:
    velocity_outbound (float): Outbound velocity (fraction of c)
    velocity_return (float): Return velocity (fraction of c)
    journey_time_earth (float): Total time measured on Earth
    Returns:
    float: Time experienced by traveling twin
    """
    c = 299792458
    v_out = velocity_outbound * c
    v_ret = velocity_return * c
    
    gamma_out = 1 / np.sqrt(1 - (v_out**2 / c**2))
    gamma_ret = 1 / np.sqrt(1 - (v_ret**2 / c**2))
    
    # Calculate proper time for traveling twin
    traveler_time_outbound = journey_time_earth / (2 * gamma_out)
    traveler_time_return = journey_time_earth / (2 * gamma_ret)
    
    return traveler_time_outbound + traveler_time_return

# Example simulation
earth_time = 10  # years
velocities = np.linspace(0.1, 0.99, 100)
traveler_times = [
    simulate_twin_paradox(v, v, earth_time) 
    for v in velocities
]

plt.figure(figsize=(10, 6))
plt.plot(velocities, traveler_times)
plt.xlabel('Velocity (fraction of c)')
plt.ylabel('Traveler Time (years)')
plt.title('Twin Paradox: Time Dilation Effect')
plt.grid(True)
plt.show()