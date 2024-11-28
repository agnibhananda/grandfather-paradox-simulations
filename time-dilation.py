import numpy as np
import matplotlib.pyplot as plt

def calculate_time_dilation(velocity, proper_time):
    """
    Calculate time dilation based on Special Relativity
    
    Parameters:
    velocity (float): Velocity in meters per second
    proper_time (float): Time measured in the stationary frame
    
    Returns:
    float: Dilated time in the moving frame
    """
    c = 299792458  # Speed of light in m/s
    gamma = 1 / np.sqrt(1 - (velocity**2 / c**2))
    dilated_time = proper_time * gamma
    return dilated_time

# Example calculation
velocities = np.linspace(0, 0.99*299792458, 1000)
proper_time = 1.0  # 1 second

# Calculate dilated times
dilated_times = [calculate_time_dilation(v, proper_time) 
                for v in velocities]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(velocities/299792458, dilated_times)
plt.xlabel('Velocity (fraction of c)')
plt.ylabel('Dilated Time (seconds)')
plt.title('Time Dilation Effect')
plt.grid(True)
plt.show()