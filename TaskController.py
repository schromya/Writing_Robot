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

    def objective_function(self, x, y, q, dq, Fz_d, Kp, Kd):
        """
        The objective function to minimize:
        J = w1 * ||u||^2 + w2 * (Fz - Fz_d)^2 + w3 * ||y'' - Kp * y - Kd * y'||^2
        """
        # Extracting optimization variables
        u = x[:len(q)]  # Control input vector (forces/torques)
        Fz = x[len(q):len(q) + 1]  # Vertical force (scalar)
        ddy = x[len(q) + 1:]  # Trajectory (e.g., positions)

        dy = self.panda_mech.solve_fk_velocity(q, dq)

        # The term ||u||^2
        u_norm = np.linalg.norm(u)**2
        
        # The term (Fz - Fz_d)^2
        Fz_term = (Fz - Fz_d)**2

        # The term ||y'' - Kp * y - Kd * y'||^2 (approximating y'' by finite difference)
        y_term = np.linalg.norm(ddy - Kp * y - Kd * dy)**2

        # Objective function to minimize
        return self.w1 * u_norm + self.w2 * Fz_term + self.w3 * y_term

    def in_constraint_upper(self, x, q):
        """Inequality constraint: upper bound for the control input u"""
        u = x[:len(q)]
        return 2000 - u

    def in_constraint_lower(self, x, q):
        """Inequality constraint: lower bound for the control input u"""
        u = x[:len(q)]
        return u - 500  # Example: lower bound for control input norm

    def equality_constraint(self, x, q, dq, ddq, J):
        """
        Equality constraint: M * q'' + C * q' + G = u + J.T * Fz
        """
        u = x[:len(q)]  # Control input
        Fz = x[len(q):len(q) + 1]  # Vertical force
        ddy = x[len(q) + 1:]

        # dJ = self.panda_mech.get_Jacobian_derivative(q)
        # ddq = (ddy - dJ * dq) / J
        
        # Get dynamics (M, C, G)
        M = self.panda_mech.get_M(q)  # Mass matrix
        C = self.panda_mech.get_C(q, dq)  # Coriolis matrix
        G = self.panda_mech.get_G(q)  # Gravity vector

        # Compute the left and right sides of the equation
        left_side = M @ ddq + C @ dq + G

        F = np.array([[0], [0], Fz, [0], [0], [0]])
        right_side = u + J.T @ F

        # The equality constraint should be zero
        #return np.allclose(left_side, right_side)
        # Absolute sum so that can minimize
        return np.sum(np.abs(left_side - right_side))


    def optimize(self, Y, Y_des, q, dq, ddq, Fz_d):
        """Solve the optimization problem to get the optimal u, Fz, and trajectory."""
        
        y = Y - Y_des
        ddy_dim = 6 # X, Y, Z, roll, pitch, yaw
        Kp = np.array([10] * ddy_dim)   # Proportional gain
        Kd = np.array([1] * ddy_dim)  # Derivative gain

        J = self.panda_mech.get_Jacobian(q)

        # Initial guess for optimization (u, Fz, y'')
        x0 = np.array([1000] * 7 + [1] + [10] * 6)

        #np.zeros(len(q) + 1 + ddy_dim)  # Initial guess for u, Fz, and trajectory y

        # Define the bounds for u and Fz (optional)
        #bounds = [(None, None)] * len(q) + [(None, None)] * 1 + [(None, None)] * ddy_dim

        # Define constraints
        cons = [{'type': 'ineq', 'fun': self.in_constraint_upper, 'args': (q, )},
                {'type': 'ineq', 'fun': self.in_constraint_lower, 'args': (q, )},
                {'type': 'eq', 'fun': self.equality_constraint, 'args': (q, dq, ddq, J)}]

        # Minimize the objective function using a suitable optimizer (e.g., SLSQP)
        result = minimize(self.objective_function, x0, args=(y, q, dq, Fz_d, Kp, Kd, ),
                          method='SLSQP', constraints=cons, )

        # The result will contain the optimized u, Fz, and y (trajectory)
        u_opt = result.x[:len(q)]  # Optimized control input
        Fz_opt = result.x[len(q):len(q) + 1]  # Optimized vertical force
        ddy_opt = result.x[len(q) + 1:]  # Optimized trajectory
        u = u_opt.T
        print("Opt Fz_opt", Fz_opt.round(2))
        print("Opt ddy_opt", ddy_opt.round(2))
        print("Opt u", u.round(2))
        return u