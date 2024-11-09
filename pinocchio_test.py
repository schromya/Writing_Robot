import pinocchio
import os

urdf_filename = 'panda_arm.urdf'
model = pinocchio.buildModelFromUrdf(urdf_filename, pinocchio.JointModelFreeFlyer())
data = model.createData()
print('model name: ' + model.name)

q = pinocchio.neutral(model)       # Joint positions
v = pinocchio.utils.zero(model.nv) # Joint velocities

pinocchio.ccrba(model, data, q, v)
print(data.Ig)

pinocchio.centerOfMass(model, data, q)