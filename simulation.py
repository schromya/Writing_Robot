import pybullet as p
import time
import pybullet_data

physics_client = p.connect(p.GUI) # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, 0) # No gravity since we are doing our own gravity dynamics

# Load ground
plane_ID = p.loadURDF("plane.urdf")

# Load robot
start_pos = [0,0,0]
start_orientation = p.getQuaternionFromEuler([0,0,0])
robot = p.loadURDF("panda_arm.urdf", start_pos, start_orientation)

# Keep simulation up to see URDF
while(True):
    continue
p.disconnect()
