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
robot = p.loadURDF("panda_arm_no_hand.urdf", start_pos, start_orientation, useFixedBase=True)

NUM_JOINTS = 7
JOINTS = [i for i in range(NUM_JOINTS)]

# Start robot in "default" position to not exceed joint limits
default_q = [0, -0.785, 0, -2.355, 0, 1.57, 0.785]
for i in range(NUM_JOINTS):
    p.resetJointState(
        bodyUniqueId = robot,
        jointIndex = i,
        targetValue = default_q[i]
    )

table = p.loadURDF("writing_surface.urdf", [2,0,0], start_orientation, useFixedBase=True)


Kp = [900.0, 900.0, 900.0, 900.0, 375.0, 225.0, 100.0] #[700, 700, 700, 900, 700, 500, 300]
Kd = [45.0, 45.0, 45.0, 45.0, 15.0, 15.0, 10.0] #[45.0, 45.0, 45.0, 45.0, 15.0, 15.0, 10.0] 


# Desired joint positions
q_des = [1, -0.5, 0.1, -2, 0.1, 1.4, 0.5]


# Let simulation run a bit before starting movement
for _ in range(100):
    p.stepSimulation() # Default is 1/240hz

    time.sleep(1/240)  # Match step simulation


# Step the simulation for a while to observe the effect
while(True):

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

    print("q", q)
    print("u", u)

    p.stepSimulation() # Default is 1/240hz

    time.sleep(1/240)  # Match step simulation



p.disconnect()
