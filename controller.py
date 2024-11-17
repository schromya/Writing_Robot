import numpy as np
from PandaMechanics import PandaMechanics

def PD(q:np.array, dq:np.array, q_des:np.array):
    """
    Given the current joint angles, velocity, and
    desired joint angles, returns the torque needed for 
    each joint using PD control method.
    """

    # Last joint (doesn't really matter) and makes everything go funky so leaving at 0
    Kp = np.array([1000.0, 1000.0, 900.0, 1000.0, 1000.0, 1000.0, 0])
    Kd = np.array([20, 20, 20, 20, 10, 10, 0])
    
    e = q - q_des
    u = -Kp * e - Kd * dq

    return u

def PD_gravity(q:np.array, dq:np.array, q_des:np.array):
    """
    Given the current joint angles, velocity, and
    desired joint angles, returns the torque needed for 
    each joint using PD + Gravity control method.
    """

    # Last joint (doesn't really matter) and makes everything go funky so leaving at 0
    Kp = np.array([1000.0, 1000.0, 900.0, 1000.0, 1000.0, 1000.0, 0])
    Kd = np.array([20, 20, 20, 20, 10, 10, 0])
    
    panda_mech = PandaMechanics()
    G = panda_mech.get_G(q)

    e = q - q_des
    u = -Kp * e - Kd * dq + G

    print("e", e.round(decimals=2))
    print("u", u.round(decimals=2))

    return u

