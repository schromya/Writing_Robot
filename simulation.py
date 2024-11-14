import pybullet as p
import time
import math
import pybullet_data

from ik import get_joint_positon


def get_trajectory_point(t):
    """
    Returns desired position at time t (seconds) to make circular trajectory
    """
    r = 0.25
    w = 1 # rad/s

    y_des = [r* math.cos(w*t) + 0.4, r*math.sin(w*t), 0.5] # X, Y, Z
    return y_des




physics_client = p.connect(p.GUI) # or p.DIRECT for non-graphical version

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)



# Load ground
plane_ID = p.loadURDF("plane.urdf")

# Load robot
start_pos = [0,0,0]
start_orientation = p.getQuaternionFromEuler([0,0,0])
robot = p.loadURDF("panda_arm_no_hand.urdf", start_pos, start_orientation, useFixedBase=True)
num_joints = p.getNumJoints(robot)
print(f"Number of Joints: {num_joints}")

for joint_index in range(num_joints):
    joint_info = p.getJointInfo(robot, joint_index)
    print(f"Joint Index: {joint_info[0]}, Joint Name: {joint_info[1].decode('utf-8')}, Joint Type: {joint_info[2]}")


NUM_JOINTS = 7
JOINTS = [i for i in range(NUM_JOINTS)]

# Start robot in "default" position to not exceed joint limits
default_q = [0, -0.785, 0, -2.355, 0, 1.57, 0.785]
q = default_q
for i in range(NUM_JOINTS):
    p.resetJointState(
        bodyUniqueId = robot,
        jointIndex = i,
        targetValue = default_q[i]
    )

table = p.loadURDF("writing_surface.urdf", [2,0,0], start_orientation, useFixedBase=True)


# Last joint (doesn't really matter) and makes everything go funky so leaving at 0
# Kp = [1500.0, 1500.0, 900.0, 1500.0, 3000.0, 2000.0, 0] 
# Kd = [0, 0, 0, 0, 0, 0, 0] 

Kp = [1000.0, 1000.0, 900.0, 1000.0, 1000.0, 1000.0, 0] 
Kd = [20, 20, 20, 20, 10, 10, 0] 

# Desired joint positions
#q_des = [1, -0.5, 0.1, -2, 0.4, 1.4, 0.5]




# Let simulation run a bit before starting movement
for _ in range(100):
    p.stepSimulation() # Default is 1/240hz

    time.sleep(1/240)  # Match step simulation

time_sec = 0
# Step the simulation for a while to observe the effect
while(True):

    y_des = get_trajectory_point(time_sec)
    q_des = get_joint_positon(q=q, x=y_des[0], y=y_des[1], z=y_des[2])

    # TODO: MAKE THESE NUMPY ARRAYS FOR matrix multiplication and speed
    q = [p.getJointState(robot, i)[0] for i in JOINTS]
    dq = [p.getJointState(robot, i)[1] for i in JOINTS]
    e = [q[i] - q_des[i] for i in JOINTS]

    u = [-Kp[i] * e[i] - Kd[i] * dq[i] for i in JOINTS]
    
    p.setJointMotorControlArray(
        bodyIndex=robot,
        jointIndices=JOINTS, 
        controlMode=p.TORQUE_CONTROL,
        forces = u
    )

    print("----")
    print("q", [round(num, 2) for num in q])
    print("e", [round(num, 2) for num in e])
    print("u", [round(num, 2) for num in u])

    p.stepSimulation() # Default is 1/240hz
    time_sec += 1/240
    time.sleep(1/240)  # Match step simulation



p.disconnect()
