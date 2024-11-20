import math


def circle_trajectory(t:float) -> float:
    """
    Returns desired position at time t (seconds) to make circular trajectory
    with end effector.
    """
    r = 0.25  # meters
    w = 0.50  # rad/s

    Y_des = [r* math.cos(w*t) + 0.4, r*math.sin(w*t), 0.5] # X, Y, Z
    return Y_des


def point_trajectory(t) -> float:
    """
    
    """

    if t >= 3:
        Y_des = [0.4, 0.0, 0.55]
    else:
        Y_des =  [0.3, 0.0 ,0.55]

    return Y_des
    
