import numpy as np
from PandaMechanics import PandaMechanics
from controller import CLF_QP_with_error
from PandaPlot import PandaPlot

# Initialize robot mechanics and controller
robot_mechanics = PandaMechanics()


# Simulation parameters
dt = 0.01
num_steps = 1000

# Initial state
q = np.array([0, -0.785, 0, -2.355, 0, 1.57, 0.785])  # Example initial joint positions
dq = np.zeros_like(q)

# Desired pose (end effector position)
desired_pose = np.array([0.3, 0.0, 0.5])  # Start with a position above the table

# Simulation log
positions = []
velocities = []
forces = []

# Simulation loop
for step in range(num_steps):
    # Solve forward kinematics to get current end effector position
    end_effector_position = robot_mechanics.solve_fk(q)
    
    # Determine contact state (e.g., when end effector reaches the table height)
    contact_state = end_effector_position[2] <= 0.5  # Table height is 0.5m

    # Adjust desired pose based on contact state
    if contact_state:
        # Maintain desired x, y and contact force in z direction
        desired_force = np.array([0.0, 0.0, 1.0])  # fz = 1.0 N when in contact
    else:
        desired_force = np.array([0.0, 0.0, 0.0])  # fz = 0 N when not in contact

    # Compute control torques using the CLFQP controller
    torques = CLF_QP_with_error(q, dq, desired_pose, contact_state)

    # Simulate the robot's dynamics
    M = robot_mechanics.get_M(q)
    C = robot_mechanics.get_C(q, dq)
    G = robot_mechanics.get_G(q)
    ddq = np.linalg.solve(M, torques - C @ dq - G)

    # Update states using simple integration
    dq += ddq * dt
    q += dq * dt

    # Log data for visualization
    positions.append(q.copy())
    velocities.append(dq.copy())
    forces.append(desired_force.copy())

    # Print debug information
    if step % 100 == 0:
        print(f"Step {step}: Position = {end_effector_position}, Contact = {contact_state}")

# # Visualization
# positions = np.array(positions)
# velocities = np.array(velocities)
# forces = np.array(forces)

# plotter = PandaPlot()
# plotter.plot_joint_trajectories(positions, title="Joint Trajectories")
# plotter.plot_end_effector_trajectory(positions, title="End Effector Trajectory")