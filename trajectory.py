import math

def get_trajectory_point(t):
    """
    Returns desired position at time t (seconds) to make circular trajectory
    """
    r = 0.25
    w = 0.5 # rad/s

    y_des = [r* math.cos(w*t) + 0.4, r*math.sin(w*t), 0.5] # X, Y, Z
    return y_des