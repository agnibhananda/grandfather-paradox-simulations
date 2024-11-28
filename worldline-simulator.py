import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_worldline(t, x0, v, acceleration=0):
    """
    Generate a worldline for an object in spacetime
    
    Parameters:
    t (array): Time points
    x0 (float): Initial position
    v (float): Initial velocity
    acceleration (float): Constant acceleration
    
    Returns:
    tuple: Arrays of x, y positions
    """
    x = x0 + v*t + 0.5*acceleration*t**2
    return t, x

# Time points
t = np.linspace(0, 10, 1000)

# Generate different worldlines
worldline1 = generate_worldline(t, 0, 0.5)  # Constant velocity
worldline2 = generate_worldline(t, 0, 0, 0.1)  # Accelerating
worldline3 = generate_worldline(t, 5, -0.3)  # Different initial position

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(*worldline1, label='Constant Velocity')
plt.plot(*worldline2, label='Accelerating')
plt.plot(*worldline3, label='Different Initial Position')
plt.xlabel('Time')
plt.ylabel('Space')
plt.title('Worldlines in Spacetime')
plt.legend()
plt.grid(True)
plt.show()