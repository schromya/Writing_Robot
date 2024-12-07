from scipy.optimize import minimize

class TaskSpaceController:
    def _init_(self, panda_mech, w1=1.0, w2=1.0, w3=1.0):
        # Initialize Panda mechanics object and weights
        self.panda_mech = panda_mech
        self.w1 = w1  # Weight for u
        self.w2 = w2  # Weight for Fz
        self.w3 = w3  # Weight for y'' - Kp * y - Kd * y'

    def objective_function(self, x, q, dq, q_des, dq_des, ddq_des, Fz_d, J, Kp, Kd):
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
        y_ddot = np.diff(y, 2)  # Second derivative (approximating y'')
        y_term = np.linalg.norm(y_ddot - Kp * y - Kd * np.diff(y))**2

        # Objective function to minimize
        return self.w1 * u_norm + self.w2 * Fz_term + self.w3 * y_term

    def in_constraint_upper(self, x):
        """Inequality constraint: upper bound for the control input u"""
        u = x[:len(q)]
        return 2000 - np.linalg.norm(u)  # Example: upper bound for control input norm

    def in_constraint_lower(self, x):
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
        right_side = u + J.T @ Fz
        
        # The equality constraint should be zero
        return np.allclose(left_side, right_side)

    def get_Jacobian_dot(self, q, dq):
        """Computes the time derivative of the Jacobian."""
        model, data = self.panda_mech.get_robot_model_data()  # Assuming you have this method
        J = get_Jacobian(q)  # Jacobian (define this or use Pinocchio)
        J_dot = pin.computeFrameJacobianDot(model, data, q, dq, pin.ReferenceFrame.LOCAL)
        return J_dot

    def optimize(self, q, dq, q_des, dq_des, ddq_des, Fz_d, J, Kp, Kd):
        """Solve the optimization problem to get the optimal u, Fz, and trajectory."""
        # Initial guess for optimization (u, Fz, y)
        x0 = np.zeros(len(q) + 1 + len(q))  # Initial guess for u, Fz, and trajectory y

        # Define the bounds for u and Fz (optional)
        bounds = [(None, None)] * len(q) + [(None, None)] * 1 + [(None, None)] * len(q)

        # Define constraints
        cons = [{'type': 'ineq', 'fun': self.in_constraint_upper},
                {'type': 'ineq', 'fun': self.in_constraint_lower},
                {'type': 'eq', 'fun': self.equality_constraint, 'args': (q, dq, ddq_des, J)}]

        # Minimize the objective function using a suitable optimizer (e.g., SLSQP)
        result = minimize(self.objective_function, x0, args=(q, dq, q_des, dq_des, ddq_des, Fz_d, J, Kp, Kd),
                          method='SLSQP', constraints=cons, bounds=bounds)

        # The result will contain the optimized u, Fz, and y (trajectory)
        u_opt = result.x[:len(q)]  # Optimized control input
        Fz_opt = result.x[len(q):len(q) + 1]  # Optimized vertical force
        y_opt = result.x[len(q) + 1:]  # Optimized trajectory
        u = u_opt.T[0]
        return u