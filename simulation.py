import pybullet as p
import time

import pybullet_data
import numpy as np

from PandaMechanics import PandaMechanics
from trajectory import get_trajectory_point




physics_client = p.connect(p.GUI) # or p.DIRECT for non-graphical version

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)



# Load ground
plane_ID = p.loadURDF("plane.urdf")

# Load robot
start_pos = [0,0,0]
start_orientation = p.getQuaternionFromEuler([0,0,0])
robot = p.loadURDF("urdfs/panda_arm_no_hand.urdf", start_pos, start_orientation, useFixedBase=True)
num_joints = p.getNumJoints(robot)

NUM_JOINTS = 7
JOINTS = [i for i in range(NUM_JOINTS)]

# Start robot in "default" position to not exceed joint limits
default_q = np.array([0, -0.785, 0, -2.355, 0, 1.57, 0.785])
q = default_q
for i in range(NUM_JOINTS):
    p.resetJointState(
        bodyUniqueId = robot,
        jointIndex = i,
        targetValue = default_q[i]
    )

table = p.loadURDF("urdfs/writing_surface.urdf", [1.0,0,0], start_orientation, useFixedBase=True)


# Last joint (doesn't really matter) and makes everything go funky so leaving at 0
Kp = np.array([1000.0, 1000.0, 900.0, 1000.0, 1000.0, 1000.0, 0])
Kd = np.array([20, 20, 20, 20, 10, 10, 0])


panda_mech = PandaMechanics()


simulation_time = 0
TIME_STEP = 1/240
p.setTimeStep(TIME_STEP)
while(True):

    y_des = get_trajectory_point(simulation_time)
    q_des = panda_mech.solve_ik(q=q, x=y_des[0], y=y_des[1], z=y_des[2])

    q = np.array([p.getJointState(robot, i)[0] for i in JOINTS])
    dq = np.array([p.getJointState(robot, i)[1] for i in JOINTS])

    e = q - q_des
    u = -Kp * e - Kd * dq
    
    p.setJointMotorControlArray(
        bodyIndex=robot,
        jointIndices=JOINTS, 
        controlMode=p.TORQUE_CONTROL,
        forces = u
    )

    print("----")
    print("q", q.round(2))
    print("e", e.round(2))
    print("u", u.round(2))

    p.stepSimulation() # Default is 1/240hz
    simulation_time += TIME_STEP
    time.sleep(TIME_STEP)  # Match simulation with real-life time



p.disconnect()
