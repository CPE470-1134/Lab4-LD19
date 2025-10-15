import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    
    def __init__(self):
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': 'polar'})
        self.scat = self.ax.scatter([], [], c=[], cmap='viridis', s=10)
        self.ax.set_ylim(0, 12000)  # Assuming max distance is 12 M
        self.ax.set_theta_zero_location('N')
        self.ax.set_theta_direction(-1)  # Left Handed
        self.ax.set_title("Measured LD19 360° Scan")
        plt.ion() # Interactive mode
        plt.show()

    def update(self, points):
        if not points:
            return
        
        
        print(f"Updating plot with {len(points)} points")
        
        # Convert angles to radians for polar plot
        angles = np.radians([p.angle for p in points])
        # Get distances and intensities
        distances = [p.distance for p in points]
        intensities = [p.intensity for p in points]

        self.scat.set_offsets(np.c_[angles, distances])
        self.scat.set_array(np.array(intensities))
        self.ax.figure.canvas.draw()
        self.ax.figure.canvas.flush_events()
        #plt.pause(0.1)  # Small pause to update the plot

    def clear(self):
        self.scat.set_offsets(np.c_[[], []])
        self.scat.set_array(np.array([]))
        self.ax.figure.canvas.draw()
        self.ax.figure.canvas.flush_events()

    def reset(self):
        self.clear()
        
    def close(self):
        plt.ioff()
        plt.close(self.fig)
        
    def save(self, filename):
        self.fig.savefig(filename)
        