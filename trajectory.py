import math
import numpy as np


def circle_trajectory(t:float) -> np.array:
    """
    Returns desired position at time t (seconds) to make circular trajectory
    with end effector.
    """
    r = 0.15  # circle radius (meters)
    w = 0.50  # rad/s

    Y_des = np.array([r* math.cos(w*t) + 0.4, r*math.sin(w*t), 0.62]) # X, Y, Z
    return Y_des


def point_trajectory(t) -> np.array:
    """
    
    """


    # if t >= 3:
    #     return np.array([0.4, 0.0, 0.55])
    
    return np.array([0.3, 0.0 ,0.55])

