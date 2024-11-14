
  
import numpy as np
from numpy.linalg import norm, solve

import pybullet as p
import time
import pybullet_data

import pinocchio as pin


def get_joint_positon(q:list, x:float, y:float, z:float):
    """
    Give the current joint positions (q in radians) 
    and the desired cartesizan positions, 
    returns the end effector position
    The orientation of the end effector is downward.
    """
    q = np.array(q)
    model =  pin.buildModelFromUrdf('panda_arm_no_hand.urdf')
    data = model.createData()

    JOINT_ID = model.njoints - 1
    oMdes = pin.SE3( np.array([ # Rotation matrix (facing down)
                        [1, 0, 0],
                        [0, -1, 0],
                        [0, 0, -1]
                    ]), 
                    np.array([x, y,  z]) # [X,Y, Z] # Default positions
                    )

   
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


    if success:
        print("Convergence achieved!")
    else:
        print("\nWarning: the iterative algorithm has not reached convergence to the desired precision")

    print('\nresult: %s' % q.flatten().tolist())
    print('\nfinal error: %s' % err.T)

    return q.flatten().tolist()
