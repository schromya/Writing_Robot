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

table = p.loadURDF("writing_surface.urdf", [0.7,0,0], start_orientation, useFixedBase=True)

NUM_JOINTS = 7
JOINTS = [i for i in range(NUM_JOINTS)]


Kp = [900.0, 900.0, 900.0, 900.0, 375.0, 225.0, 100.0] #[700, 700, 700, 900, 700, 500, 300]
Kd =  [20, 5, 7, 7, 3, 3, 0.1] #[45.0, 45.0, 45.0, 45.0, 15.0, 15.0, 10.0] 

# Desired joint positions
q_des = [0, -0.785, 0, -2.355, 0, 1.57, 0.785]

# Check position
# p.setJointMotorControlArray(
#         bodyIndex=robot,[900.0, 900.0, 900.0, 900.0, 375.0, 225.0, 100.0]
#         jointIndices=[0, 1, 2, 3, 4, 5, 6], 
#         controlMode=p.POSITION_CONTROL,
#         targetPositions= q_des,
#         targetVelocities = [0.5 for _ in JOINTS],
# )



# Step the simulation for a while to observe the effect
while(True):

    # TODO: MAKE THESE NUMPY ARRAYS FOR matrix multiplication and speed
    q = [p.getJointState(robot, i)[0] for i in JOINTS]
    dq = [p.getJointState(robot, i)[1] for i in JOINTS]
    e = [q_des[i] - q[i] for i in JOINTS]

    u = [Kp[i] * e[i] + Kd[i] * dq[i] for i in JOINTS]
    
    p.setJointMotorControlArray(
        bodyIndex=robot,
        jointIndices=JOINTS, 
        controlMode=p.TORQUE_CONTROL,
        forces = u
    )


    p.stepSimulation() # Default is 1/240hz

    time.sleep(1/240)  # Match step simulation



p.disconnect()
