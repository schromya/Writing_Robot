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


# p.setJointMotorControl2(bodyUniqueId=robot, 
# jointIndex=1, 
# controlMode=p.VELOCITY_CONTROL,
# targetVelocity = 1,
# force = 500)

# Step the simulation for a while to observe the effect
for _ in range(10000):
    p.setJointMotorControl2(
        bodyUniqueId=robot,
        jointIndex=1, 
        controlMode=p.TORQUE_CONTROL,
        force=240
    )
    p.stepSimulation() # Default is 1/240hz
    time.sleep(1/240)  # Match step simulation

# Keep simulation up to see URDF
while(True):
    continue
p.disconnect()
