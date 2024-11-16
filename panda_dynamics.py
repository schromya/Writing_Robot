import pinocchio as pin
import numpy as np

# Load the robot model from the URDF file and create data
model = pin.buildModelFromUrdf('urdfs/panda_arm_no_hand.urdf')
data = model.createData()

# Use the default configuration for the URDF, which is typically the zero position
q = np.zeros(model.nq)  # Default joint positions (home or zero configuration)
qdot = np.zeros(model.nv)  # Zero joint velocities for this test

# Compute G(q), the generalized gravity torque vector
G = pin.computeGeneralizedGravity(model, data, q)
print('G(q) for default configuration:', G)

# Compute M(q), the joint space inertia matrix
M = pin.crba(model, data, q)
print('M(q) for default configuration:\n', M)

# Compute C(q, qdot), the Coriolis matrix
C = pin.computeCoriolisMatrix(model, data, q, qdot)
print('C(q, qdot) for default configuration (with qdot=0):\n', C)
