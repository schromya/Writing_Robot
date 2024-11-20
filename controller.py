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

    return u

def CLF_QP_with_error(q: np.array, dq: np.array, q_des: np.array, dq_des: np.array, ddq_des: np.array, Fz: float, J: np.array):
    """
    Control Lyapunov Function - Quadratic Program (CLF-QP) controller with explicit
    error term and gravitational matrix G.

    Parameters:
    - q: Current joint angles
    - dq: Current joint velocities
    - q_des: Desired joint angles
    - dq_des: Desired joint velocities
    - ddq_des: Desired joint accelerations
    - Fz: Desired force in the Z direction
    - J: Jacobian of the end effector
    """
    panda_mech = PandaMechanics()
    M = panda_mech.get_M(q)
    C = panda_mech.get_C(q, dq)
    G = panda_mech.get_G(q)

    # Make sure these are all column vector
    G = G[:, np.newaxis] # (TODO: do this in PandaMech?)
    q = q[:, np.newaxis]
    dq = dq[:, np.newaxis]
    q_des = q_des[:, np.newaxis]
    dq_des = dq_des[:, np.newaxis]
    ddq_des = ddq_des[:, np.newaxis]
 
    
    # Error terms
    e = q - q_des  # Position error
    print("q", q)
    print("q_des", q_des)
    print("e", e)
    de = dq - dq_des  # Velocity error

    # Weight matrices for QP formulation
    Kp = np.eye(len(q)) * 50.0  # Proportional gain
    Kd = np.eye(len(dq)) * 20.0  # Derivative gain
    Q = np.eye(len(ddq_des)) * 1.0  # Weight on ddq
    R = np.eye(len(dq)) * 10.0  # Regularization weight

    # Desired joint-space acceleration (with error terms included)
    ddq_ref = ddq_des - Kp @ e - Kd @ de

 

    # Quadratic cost function (to minimize norm of accelerations)
    H = 2 * (M + Q)

    
    F = np.array([[0], [0], [Fz]])
    print("F", F)

    f = -(2 * (M @ ddq_ref + C @ dq + G - J.T @ F).T)
    #f = -(2 * (M @ ddq_ref + C @ dq + G - J.T @ np.array([[0], [0], [Fz], [0], [0], [0]])).T)

    print("f",f)
    # Solve QP problem for optimal joint accelerations
    ddq_star = np.linalg.solve(H, -f)


    # Compute torques
    #u = M @ ddq_star + C @ dq + G - J.T @ np.array([0, 0, Fz])
    # print("J1", J.T @ np.array([[0], [0], [Fz], [0], [0], [0]]))
    # print("M @ ddq_star", M @ ddq_star)
    u = M @ ddq_star + C @ dq + G - J.T @ np.array([[0], [0], [Fz], [0], [0], [0]])
    # print("---u", u)

    
    return u
