import numpy as np

import pybullet as p
import time
import pybullet_data


from ik import get_joint_positon

q_curr = [0, -0.785, 0, -2.355, 0, 1.57, 0.785] # Starting position
q = get_joint_positon(q=q_curr, x= 0.31, y=0.00, z=0.5)
print(q)
print("------------------")

physics_client = p.connect(p.GUI) # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Load ground
plane_ID = p.loadURDF("plane.urdf")

# Load robot
start_pos = [0,0,0]
start_orientation = p.getQuaternionFromEuler([0,0,0])
robot = p.loadURDF("panda_arm_no_hand.urdf", start_pos, start_orientation, useFixedBase=True)


#Check position
p.setJointMotorControlArray(
        bodyIndex=robot,
        jointIndices=[0, 1, 2, 3, 4, 5, 6], 
        controlMode=p.POSITION_CONTROL,
        targetPositions= q,
        targetVelocities = [0.6481366396349811, 1.2038791434804241, -0.7009613424828351, 2.0968243484246685, -0.7331872802150904, -1.1187633910821557, -0.020670192679890943],
)


# Step the simulation for a while to observe the effect
while(True):
    p.stepSimulation() # Default is 1/240hz
    time.sleep(1/240)  # Match step simulation



p.disconnect()
