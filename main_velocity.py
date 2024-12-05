"""
Runs simulation of Panda 7-DOF robot arm following trajectory
"""

import pybullet as p
import pybullet_data
import numpy as np
import time

from PandaMechanics import PandaMechanics
from PandaPlot import PandaPlot
from trajectory import circle_trajectory, point_trajectory, svg_trajectory
from controller import PD, PD_gravity, CLF_QP_with_error, PD_velocity


# Set up simulator
TIME_STEP = 1/1000
physics_client = p.connect(p.GUI) 
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
p.setTimeStep(TIME_STEP)
p.resetDebugVisualizerCamera(cameraDistance=1,
                             cameraYaw=-20,
                             cameraPitch=-40,
                             cameraTargetPosition=[0, 0, 0.6])

# Load URDFs
plane_ID = p.loadURDF("plane.urdf")
start_pos = [0,0,0]
start_orientation = p.getQuaternionFromEuler([0,0,0])
robot = p.loadURDF("urdfs/panda_arm_no_hand2.urdf", start_pos, start_orientation, useFixedBase=True)
table = p.loadURDF("urdfs/writing_surface.urdf", [0.45,0,0], start_orientation, useFixedBase=True)


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

while(True):
    
    # Check for contact points visualize them
    contact_points = p.getContactPoints(bodyA=robot, bodyB=table)
    for contact in contact_points:
        contact_position = contact[5]  # Contact position in world coordinates (x, y, z)
        
        p.addUserDebugLine(
            lineFromXYZ=contact_position,
            lineToXYZ=(contact_position[0], contact_position[1], contact_position[2] + 0.001),
            lineColorRGB=[1, 0, 0],
            lineWidth=5,
            lifeTime=100,  # Seconds
        )

    Y = panda_mech.solve_fk(q)

    # print("Z", Y[2])
    contact_state = Y[2] <= 0.7  # For buffer (Table height is 0.62m)
    Fz = 1 if contact_state else 0
    

    #Y_des = circle_trajectory(simulation_time)
    #Y_des = point_trajectory(simulation_time)
    Y_des = svg_trajectory(simulation_time)

    # print("---Fz", Fz)
    #print("---Y", Y.round(2))
    #print("---Y_des", Y_des)
    
    q_des = panda_mech.solve_ik(q=q, x=Y_des[0], y=Y_des[1], z=Y_des[2])
    q = np.array([p.getJointState(robot, i)[0] for i in JOINTS])
    dq = np.array([p.getJointState(robot, i)[1] for i in JOINTS])
    J = panda_mech.get_Jacobian(q)

    # Only plot ever so often to reduce simulation slow down
    if i % 200 == 0:
        plot.update_plot(simulation_time, q, q_des, Y, Y_des)

    #u = PD(q, dq, q_des)
    #u = PD_gravity(q, dq, q_des)
    v = PD_velocity(q, dq, q_des)
    #print("----U",  u.round(2))
    
    p.setJointMotorControlArray( bodyIndex=robot, jointIndices=JOINTS, 
        controlMode=p.VELOCITY_CONTROL, targetVelocities = v)

    p.stepSimulation() # Default is 1/240hz
    simulation_time += TIME_STEP
    i +=1
    time.sleep(TIME_STEP)  # Match simulation with real-life time

p.disconnect()