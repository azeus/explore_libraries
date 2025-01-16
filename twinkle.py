import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create random positions for dots
n_dots = 20
x = np.random.uniform(0, 10, n_dots)
y = np.random.uniform(0, 10, n_dots)

# Create scatter plot with initial alpha (transparency)
scatter = ax.scatter(x, y, c='blue', alpha=0.5)

# Initialize phase for each dot (offset for smooth animation)
phases = np.random.uniform(0, 2 * np.pi, n_dots)


def update(frame):
    # Calculate new alpha values using sine wave
    # This creates a smooth dimming and brightening effect
    alphas = 0.5 + 0.4 * np.sin(0.1 * frame + phases)

    # Update the transparency of the dots
    scatter.set_alpha(alphas)
    return scatter,


# Create animation
anim = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()