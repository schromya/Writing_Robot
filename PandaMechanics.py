  
import numpy as np
from numpy.linalg import norm, solve

import pinocchio as pin

class PandaMechanics():
    def __init__(self):
        self.model =  pin.buildModelFromUrdf('urdfs/panda_arm_no_hand.urdf')
        self.data = self.model.createData()


    def solve_ik(self, q:np.array, x:float, y:float, z:float) -> np.array:
        """
        Given the current joint positions (q in radians) and the desired 
        cartesian positions, returns the end effector position.
        The orientation of the end effector is downward.
        """

        JOINT_ID = self.model.njoints - 1
        oMdes = pin.SE3( np.array([ # Rotation matrix (facing down)
                            [1, 0, 0],
                            [0, -1, 0],
                            [0, 0, -1]
                        ]), 
                        np.array([x, y,  z]) # EE position
                        )

        eps    = 1e-4
        IT_MAX = 10000
        DT     = 1e-1
        damp   = 1e-12

        i=0
        while True:
            pin.forwardKinematics(self.model, self.data,q)
            dMi = oMdes.actInv(self.data.oMi[JOINT_ID])
            err = pin.log(dMi).vector
            if norm(err) < eps:
                success = True
                break
            if i >= IT_MAX:
                success = False
                break
            J = pin.computeJointJacobian(self.model,self.data,q,JOINT_ID)
            v = - J.T.dot(solve(J.dot(J.T) + damp * np.eye(6), err))
            q = pin.integrate(self.model,q,v*DT)
            # if not i % 10:
            #     print('%d: error = %s' % (i, err.T))
            i += 1

        if not success:
            print("\nWarning: the iterative algorithm has not reached convergence to the desired precision")

        # print('\nresult: %s' % q.flatten())
        # print('\nfinal error: %s' % err.T)

        return np.array(q.flatten())



    def solve_fk(self, q:np.array) -> np.array:
        """
        Given the current joint positions, returns
        the end effector position.
        """

        pin.forwardKinematics(self.model, self.data, q)
        
        # # Print out the placement of each joint of the kinematic tree 
        # for name, oMi in zip(self.model.names, self.data.oMi):
        #     print(("{:<24} : {: .2f} {: .2f} {: .2f}"
        #         .format( name, *oMi.translation.T.flat )))
            
        return np.array(self.data.oMi[-1].translation.T.flat)
        


if __name__ == "__main__":
    # Example usage of This class

    q = np.array([0, -0.785, 0, -2.355, 0, 1.57, 0.785])

    panda_mechanics = PandaMechanics()

    print("FK:", panda_mechanics.solve_fk(q))

    print("IK:", panda_mechanics.solve_ik(q=q, x=0.31, y=0.00, z=0.5))

