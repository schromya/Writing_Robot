
import numpy as np
from PandaMechanics import PandaMechanics

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
    
    # Error terms
    e = q - q_des  # Position error
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
    f = -(2 * (M @ ddq_ref + C @ dq + G - J.T @ np.array([0, 0, Fz])).T)

    # Solve QP problem for optimal joint accelerations
    ddq_star = np.linalg.solve(H, -f)

    # Compute torques
    u = M @ ddq_star + C @ dq + G - J.T @ np.array([0, 0, Fz])
    return u
