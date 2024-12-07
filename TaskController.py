from scipy.optimize import minimize
import numpy as np
from PandaMechanics import PandaMechanics

class TaskSpaceController:
    def __init__(self, panda_mech, w1=1.0, w2=1.0, w3=1.0):
        # Initialize Panda mechanics object and weights
        self.panda_mech = panda_mech
        self.w1 = w1  # Weight for u
        self.w2 = w2  # Weight for Fz
        self.w3 = w3  # Weight for y'' - Kp * y - Kd * y'

    def objective_function(self, x, q, Fz_d, Kp, Kd):
        """
        The objective function to minimize:
        J = w1 * ||u||^2 + w2 * (Fz - Fz_d)^2 + w3 * ||y'' - Kp * y - Kd * y'||^2
        """
        # Extracting optimization variables
        u = x[:len(q)]  # Control input vector (forces/torques)
        Fz = x[len(q):len(q) + 1]  # Vertical force (scalar)
        y = x[len(q) + 1:]  # Trajectory (e.g., positions)

        # The term ||u||^2
        u_norm = np.linalg.norm(u)**2
        
        # The term (Fz - Fz_d)^2
        Fz_term = (Fz - Fz_d)**2

        # The term ||y'' - Kp * y - Kd * y'||^2 (approximating y'' by finite difference)

        # TODO: This isn't working correctly but keeping for now
        y_dot = np.diff(y, 1)
        y_dot= np.pad(y_dot, (0, 1), mode='constant', constant_values=0)

        y_ddot = np.diff(y, 2)  # Second derivative (approximating y'')
        y_ddot= np.pad(y_ddot, (1, 1), mode='constant', constant_values=0)
        y_term = np.linalg.norm(y_ddot - Kp * y - Kd * y_dot)**2

        # Objective function to minimize
        return self.w1 * u_norm + self.w2 * Fz_term + self.w3 * y_term

    def in_constraint_upper(self, x, q):
        """Inequality constraint: upper bound for the control input u"""
        u = x[:len(q)]
        return 2000 - np.linalg.norm(u)  # Example: upper bound for control input norm

    def in_constraint_lower(self, x, q):
        """Inequality constraint: lower bound for the control input u"""
        u = x[:len(q)]
        return np.linalg.norm(u) - 400  # Example: lower bound for control input norm

    def equality_constraint(self, x, q, dq, ddq_des, J):
        """
        Equality constraint: M * q'' + C * q' + G = u + J.T * Fz
        """
        u = x[:len(q)]  # Control input
        
        Fz = x[len(q):len(q) + 1]  # Vertical force
        q_ddot = ddq_des  # Desired acceleration (q'')
        
        # Get dynamics (M, C, G)
        M = self.panda_mech.get_M(q)  # Mass matrix
        C = self.panda_mech.get_C(q, dq)  # Coriolis matrix
        G = self.panda_mech.get_G(q)  # Gravity vector

        # Compute the left and right sides of the equation
        left_side = M @ q_ddot + C @ dq + G

        F = np.array([[0], [0], Fz, [0], [0], [0]])
        right_side = u + J.T @ F

        # The equality constraint should be zero
        #return np.allclose(left_side, right_side)
        # Absolute sum so that can minimize
        return np.sum(np.abs(left_side - right_side))


    def optimize(self, q, dq, q_des, dq_des, ddq_des, Fz_d):
        """Solve the optimization problem to get the optimal u, Fz, and trajectory."""
        
        y_dim = 6 # X, Y, Z, roll, pitch, yaw
        Kp = np.array([100] * y_dim) * 100.0  # Proportional gain
        Kd = np.array([100] * y_dim) * 1.0  # Derivative gain

        J = self.panda_mech.get_Jacobian(q)

        # Initial guess for optimization (u, Fz, y)
        x0 = np.zeros(len(q) + 1 + y_dim)  # Initial guess for u, Fz, and trajectory y

        # Define the bounds for u and Fz (optional)
        bounds = [(None, None)] * len(q) + [(None, None)] * 1 + [(None, None)] * y_dim

        # Define constraints
        cons = [{'type': 'ineq', 'fun': self.in_constraint_upper, 'args': (q, )},
                {'type': 'ineq', 'fun': self.in_constraint_lower, 'args': (q, )},
                {'type': 'eq', 'fun': self.equality_constraint, 'args': (q, dq, ddq_des, J)}]

        # Minimize the objective function using a suitable optimizer (e.g., SLSQP)
        result = minimize(self.objective_function, x0, args=(q, Fz_d, Kp, Kd, ),
                          method='SLSQP', constraints=cons, bounds=bounds)

        # The result will contain the optimized u, Fz, and y (trajectory)
        u_opt = result.x[:len(q)]  # Optimized control input
        Fz_opt = result.x[len(q):len(q) + 1]  # Optimized vertical force
        y_opt = result.x[len(q) + 1:]  # Optimized trajectory
        u = u_opt.T
        print("Opt u", u.round(2))
        return u