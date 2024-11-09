import pybullet as p
import time
import pybullet_data

physics_client = p.connect(p.GUI) # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Load ground
plane_ID = p.loadURDF("plane.urdf")

# Load robot
start_pos = [0,0,0]
start_orientation = p.getQuaternionFromEuler([0,0,0])
robot = p.loadURDF("panda_arm.urdf", start_pos, start_orientation, useFixedBase=True)

NUM_JOINTS = 7
JOINT_LIST = range(NUM_JOINTS)
Kp = 1
Kd = 1.2

# Desired joint positions
q_des = [0, -0.785, 0, -2.355, 0, 1.57, 0.785]

# Check position
p.setJointMotorControlArray(
        bodyIndex=robot,
        jointIndices=[0, 1, 2, 3, 4, 5, 6], 
        controlMode=p.POSITION_CONTROL,
        targetPositions= q_des,
        targetVelocities = [0.5 for _ in JOINT_LIST],
)



# Step the simulation for a while to observe the effect
for _ in range(1000):


    # p.setJointMotorControl2(
    #     bodyUniqueId=robot,
    #     jointIndex=1, 
    #     controlMode=p.TORQUE_CONTROL,
    #     force=240
    # )


    p.stepSimulation() # Default is 1/240hz

    time.sleep(1/240)  # Match step simulation

q = [p.getJointState(robot, i)[0] for i in JOINT_LIST]
dq = [p.getJointState(robot, i)[1] for i in JOINT_LIST]
print(q)


print(dq)


# Keep simulation up to see URDF
while(True):
    continue
p.disconnect()
