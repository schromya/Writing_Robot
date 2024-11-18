import matplotlib.pyplot as plt
import numpy as np
import time

class PandaPlot():
    """"""
        
    def __init__(self, num_joints=7):
        self.NUM_JOINTS = num_joints
        plt.ion()  
        fig, self.axes = plt.subplots(self.NUM_JOINTS, 1, figsize=(8, 12))  # One subplot per joint
        fig.tight_layout(pad=4.0)
        self.lines_q = [ax.plot([], [], label=f"Joint {i + 1} Position")[0] for i, ax in enumerate(self.axes)]
        self.lines_q_des = [ax.plot([], [], label=f"Joint {i + 1} Desired")[0] for i, ax in enumerate(self.axes)]

        self.q_history = [[] for _ in range(self.NUM_JOINTS)]
        self.q_des_history = [[] for _ in range(self.NUM_JOINTS)] 
        self.t_history = []

    def update_plot(self, t, q, q_des):
        # Update Joint Position Data
        self.t_history.append(t)
        for i in range(self.NUM_JOINTS):
            self.q_history[i].append(q[i])
            self.q_des_history[i].append(q_des[i])

        # Update Plot
        for i, ax in enumerate(self.axes):
            
            # Update existing line
            self.lines_q[i].set_data(self.t_history, self.q_history[i])  
            self.lines_q_des[i].set_data(self.t_history, self.q_des_history[i])

            # Adjust axis and labels
            ax.relim()  # Recalculate limits
            ax.autoscale_view()  # Adjust view to new data
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Position (rad)")
            ax.grid(True)
            ax.legend(loc="upper left")

        plt.pause(0.001)  # Allow time for plot updates

if __name__ == "__main__":
    # Simulated data update loop for demonstration
    plot = PandaPlot()
    t = 0
    while t < 10:  # Simulate for 10 seconds
        q = np.sin(np.linspace(0, 2 * np.pi, plot.NUM_JOINTS) + t)  # Example actual joint positions
        q_des = np.cos(np.linspace(0, 2 * np.pi, plot.NUM_JOINTS) + t)  # Example desired joint positions
        plot.update_plot(t, q, q_des)
        t += 0.1
        time.sleep(0.1)