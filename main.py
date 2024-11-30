"""
Runs simulation of Panda 7-DOF robot arm following trajectory
"""

import pybullet as p
import pybullet_data
import numpy as np
import time

from PandaMechanics import PandaMechanics
from PandaPlot import PandaPlot
from trajectory import circle_trajectory, point_trajectory
from controller import PD, PD_gravity, CLF_QP_with_error


# Set up simulator
TIME_STEP = 1/240
physics_client = p.connect(p.GUI) 
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
p.setTimeStep(TIME_STEP)

# Load URDFs
plane_ID = p.loadURDF("plane.urdf")
start_pos = [0,0,0]
start_orientation = p.getQuaternionFromEuler([0,0,0])
robot = p.loadURDF("urdfs/panda_arm_no_hand.urdf", start_pos, start_orientation, useFixedBase=True)
table = p.loadURDF("urdfs/writing_surface.urdf", [0.4,0,0], start_orientation, useFixedBase=True)

NUM_JOINTS = p.getNumJoints(robot) - 1
JOINTS = [i for i in range(NUM_JOINTS)]
simulation_time = 0
i = 0
panda_mech = PandaMechanics()
plot = PandaPlot(NUM_JOINTS)

# Start robot in "default" position to not exceed joint limits
q = np.array([0, -0.785, 0, -2.355, 0, 1.57, 0.785])
for i in range(NUM_JOINTS):
    p.resetJointState(bodyUniqueId = robot, jointIndex = i, targetValue = q[i])

for _ in range(100):
    p.stepSimulation() # Default is 1/240hz
    simulation_time += TIME_STEP
    time.sleep(TIME_STEP)  # Match simulation with real-life time

# PD controller to get to table
total_error = 10 # Large Number
while total_error > 0.001:


    Y = panda_mech.solve_fk(q)
    print("Y", Y.round(2))
    Y_des = [0.3, 0.0 ,0.55]
    q_des = panda_mech.solve_ik(q=q, x=Y_des[0], y=Y_des[1], z=Y_des[2])
    q = np.array([p.getJointState(robot, i)[0] for i in JOINTS])
    dq = np.array([p.getJointState(robot, i)[1] for i in JOINTS])


    # Only plot ever so often to reduce simulation slow down
    # if i % 80 == 0:
    #     plot.update_plot(simulation_time, q, q_des, Y, Y_des)

    u = PD(q, dq, q_des)
    #u = PD_gravity(q, dq, q_des)
    print("u", u.round(2))

    total_error = np.sum(np.square(Y_des - Y))
    print("total_error", total_error.round(2))
    print("e", (Y_des - Y).round(2))

    p.setJointMotorControlArray( bodyIndex=robot, jointIndices=JOINTS, 
        controlMode=p.TORQUE_CONTROL, forces = u)

    p.stepSimulation() # Default is 1/240hz
    simulation_time += TIME_STEP
    i +=1
    time.sleep(TIME_STEP)  # Match simulation with real-life time

print("FINISHED PD CONTROL!!!!")

# # Force controller while on table
# while True:


#     Y = panda_mech.solve_fk(q)
#     print("---Y", Y)
#     #Y_des = circle_trajectory(simulation_time)
#     Y_des = point_trajectory(simulation_time)
#     print("---Y_des", Y_des)
#     q_des = panda_mech.solve_ik(q=q, x=Y_des[0], y=Y_des[1], z=Y_des[2])
#     q = np.array([p.getJointState(robot, i)[0] for i in JOINTS])
#     dq = np.array([p.getJointState(robot, i)[1] for i in JOINTS])
#     J = panda_mech.get_Jacobian(q)
#     Fz = 1.0  # Desired force in the Z direction

#     # Only plot ever so often to reduce simulation slow down
#     # if i % 80 == 0:
#     #     plot.update_plot(simulation_time, q, q_des, Y, Y_des)

#     #u = PD(q, dq, q_des)
#     #u = PD_gravity(q, dq, q_des)
#     u = CLF_QP_with_error(q, dq, q_des, dq_des=np.zeros_like(q), ddq_des=np.zeros_like(q), Fz=Fz, J=J)

    
#     p.setJointMotorControlArray( bodyIndex=robot, jointIndices=JOINTS, 
#         controlMode=p.TORQUE_CONTROL, forces = u)

#     p.stepSimulation() # Default is 1/240hz
#     simulation_time += TIME_STEP
#     i +=1
#     time.sleep(TIME_STEP)  # Match simulation with real-life time

# p.disconnect()
