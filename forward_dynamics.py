import pinocchio as pin
import numpy as np

model =  pin.buildModelFromUrdf('urdfs/panda_arm_no_hand.urdf')
data = model.createData()

q = np.array([0, -0.785, 0, -2.355, 0, 1.57, 0.785])

print(type(q))
pin.forwardKinematics(model,data,q)
print("ee_des")
# Print out the placement of each joint of the kinematic tree
for name, oMi in zip(model.names, data.oMi):
    print(("{:<24} : {: .2f} {: .2f} {: .2f}"
          .format( name, *oMi.translation.T.flat )))