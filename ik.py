
  
import numpy as np
from numpy.linalg import norm, solve

import pybullet as p
import time
import pybullet_data

import pinocchio as pin

model =  pin.buildModelFromUrdf('panda_arm_no_hand.urdf')
data = model.createData()

JOINT_ID = model.njoints - 1
oMdes = pin.SE3( np.array([ # Rotation matrix (facing down)
                    [1, 0, 0],
                    [0, -1, 0],
                    [0, 0, -1]
                ]), 
                 np.array([0.31, 0.00,  0.5]) # [X,Y, Z] # Default positions
                 )

q = np.array([0, -0.785, 0, -2.355, 0, 1.57, 0.785]) # Starting position
print(q)
print("------------------")
eps    = 1e-4
IT_MAX = 10000
DT     = 1e-1
damp   = 1e-12

i=0
while True:
    pin.forwardKinematics(model,data,q)
    dMi = oMdes.actInv(data.oMi[JOINT_ID])
    err = pin.log(dMi).vector
    if norm(err) < eps:
        success = True
        break
    if i >= IT_MAX:
        success = False
        break
    J = pin.computeJointJacobian(model,data,q,JOINT_ID)
    v = - J.T.dot(solve(J.dot(J.T) + damp * np.eye(6), err))
    q = pin.integrate(model,q,v*DT)
    if not i % 10:
        print('%d: error = %s' % (i, err.T))
    i += 1






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

q_des = q.flatten().tolist()
if success:
    print("Convergence achieved!")
else:
    print("\nWarning: the iterative algorithm has not reached convergence to the desired precision")

print('\nresult: %s' % q.flatten().tolist())
print('\nfinal error: %s' % err.T)


pin.forwardKinematics(model,data,q)
print("ee_des")
# Print out the placement of each joint of the kinematic tree
for name, oMi in zip(model.names, data.oMi):
    print(("{:<24} : {: .2f} {: .2f} {: .2f}"
          .format( name, *oMi.translation.T.flat )))

print("----------------")
#Check position
p.setJointMotorControlArray(
        bodyIndex=robot,
        jointIndices=[0, 1, 2, 3, 4, 5, 6], 
        controlMode=p.POSITION_CONTROL,
        targetPositions= q_des,
        targetVelocities = [0.6481366396349811, 1.2038791434804241, -0.7009613424828351, 2.0968243484246685, -0.7331872802150904, -1.1187633910821557, -0.020670192679890943],
)


# Step the simulation for a while to observe the effect
while(True):
    p.stepSimulation() # Default is 1/240hz
    time.sleep(1/240)  # Match step simulation



p.disconnect()
