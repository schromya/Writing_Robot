
import matplotlib.pyplot as plt
import numpy as np
import time

class PandaPlot():
    def __init__(self, num_joints=7, max_points=500):
        self.NUM_JOINTS = num_joints
        self.DIM = 3  # Dimensions (x, y, z)
        self.max_points = max_points
        self.update_counter = 0  # Counter to control refresh rate
        plt.ion()

        # Figure for joint positions
        self.fig_joints, self.fig_axes = plt.subplots(self.NUM_JOINTS, 1, figsize=(8, 12))  # One subplot per joint
        self.fig_joints.tight_layout(pad=4.0)
        for ax in self.fig_axes:
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Position (rad)")
            ax.grid(True)
            ax.legend(loc="upper left")
            ax.set_xlim(0, 60) 
            ax.set_ylim(-3.14, 3.14) 

        # Lines for joint positions
        self.lines_q = [ax.plot([], [], color="green", label=f"Joint {i + 1} Position")[0] for i, ax in enumerate(self.fig_axes)]
        self.lines_q_des = [ax.plot([], [], color="orange", label=f"Joint {i + 1} Desired")[0] for i, ax in enumerate(self.fig_axes)]

    
        # Lines for joint positions
        self.lines_q = [ax.plot([], [], label=f"Joint {i + 1} Position")[0] for i, ax in enumerate(self.fig_axes)]
        self.lines_q_des = [ax.plot([], [], label=f"Joint {i + 1} Desired")[0] for i, ax in enumerate(self.fig_axes)]
        
        # Data for joint positions
        self.t_history = []
        self.q_history = [[] for _ in range(self.NUM_JOINTS)]
        self.q_des_history = [[] for _ in range(self.NUM_JOINTS)] 


        #################################################################################
        # Figure for xy and xz planes
        self.fig_planes, (self.ax_yx, self.ax_xz) = plt.subplots(1, 2, figsize=(12, 6))
        for ax, title, xlabel, ylabel in [(self.ax_yx, "XY Plane", "Y", "X"), (self.ax_xz, "XZ Plane", "X", "Z")]:
            ax.set_title(title)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.grid(True)
            ax.legend(loc="upper left")
            ax.set_xlim(-0.7, 0.7) 
            ax.set_ylim(0.1, 0.8) 
        
        # Invert the y for displaying letters nicely
        self.ax_yx.invert_xaxis()

        # Lines for yx and xz plots
        self.line_yx, = self.ax_yx.plot([], [], label="Y", color="green")
        self.line_yx_des, = self.ax_yx.plot([], [], label="Y_des", color="orange", linestyle="--")
        self.line_xz, = self.ax_xz.plot([], [], label="Y", color="green")
        self.line_xz_des, = self.ax_xz.plot([], [], label="Y_des", color="orange", linestyle="--")

        # Data for xz and xy plots
        self.Y_history = [[] for _ in range(self.DIM)]
        self.Y_des_history = [[] for _ in range(self.DIM)]

    def update_plot(self, t, q, q_des, Y, Y_des):

        # Update joint data
        self.t_history.append(t)
        for i in range(self.NUM_JOINTS):
            self.q_history[i].append(q[i])
            self.q_des_history[i].append(q_des[i])
        
        # Update joint plot
        for i, ax in enumerate(self.fig_axes):
            # Update existing line
            self.lines_q[i].set_data(self.t_history, self.q_history[i])  
            self.lines_q_des[i].set_data(self.t_history, self.q_des_history[i])

        #################################################################################
        # Update plane data
        for i in range(self.DIM):
            self.Y_history[i].append(Y[i])
            self.Y_des_history[i].append(Y_des[i])
        
        # Update YZ Plane
        self.line_yx.set_data(self.Y_history[1], self.Y_history[0])  # y vs x
        self.line_yx_des.set_data(self.Y_des_history[1], self.Y_des_history[0])  

        # Update XZ Plane
        self.line_xz.set_data(self.Y_history[0], self.Y_history[2])  # x vs z for Y
        self.line_xz_des.set_data(self.Y_des_history[0], self.Y_des_history[2])  # x vs z for Y_des


        #################################################################################
        # Update figures
        plt.pause(0.001)  # Allow time for plot updates

if __name__ == "__main__":
    # Simulated data update loop for demonstration
    plot = PandaPlot()
    t = 0
    while t < 10:  # Simulate for 10 seconds
        q = np.sin(np.linspace(0, 2 * np.pi, plot.NUM_JOINTS) + t)  # Example actual joint positions
        q_des = np.cos(np.linspace(0, 2 * np.pi, plot.NUM_JOINTS) + t)  # Example desired joint positions
        Y = [np.sin(t), np.cos(t), np.sin(2 * t)]  # Example Y in 3D space
        Y_des = [np.sin(t), np.cos(t), np.sin(2 * t)]  # Example Y_des in 3D space
        plot.update_plot(t, q, q_des, Y, Y_des)
        t += 0.1
        time.sleep(0.1)