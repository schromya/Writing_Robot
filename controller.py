import numpy as np
from PandaMechanics import PandaMechanics

def PD(q:np.array, dq:np.array, q_des:np.array):
    """
    Given the current joint angles, velocity, and
    desired joint angles, returns the torque needed for 
    each joint using PD control method.
    """

    # 1000 hz
    Kp = np.array([7000, 5000, 5000, 5000, 5000, 5000, 1000] )
    Kd = np.array([20, 20, 20, 20, 10, 10, 10])

    e = q - q_des
    u = -Kp * e - Kd * dq

    return u

def PD_velocity(q:np.array, dq:np.array, q_des:np.array):
    """
    Given the current joint angles, velocity, and
    desired joint angles, returns the velocity needed for 
    each joint using PD control method.
    """

    # 1000 hz
    Kp = np.array([20] * 7 )
    Kd = np.array([0.01] * 7)

    e = q - q_des
    v = -Kp * e - Kd * dq

    return v

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

    return u
