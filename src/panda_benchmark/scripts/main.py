#! /usr/bin/env python3

import rospkg
import rospy
import numpy as np

from timeit import default_timer as timer

from panda_robot import PandaArm

from trajectory import circle_trajectory, point_trajectory
from controller import PD, PD_gravity, CLF_QP_with_error
from PandaMechanics import PandaMechanics

class Simulation:
    def __init__(self, arm:PandaArm):
        self.arm = arm
        self.panda_mech = PandaMechanics()
        self.time_period = 0.001
        
        self.prev_q = np.array(arm.angles()) # Current Position
        self.q_des = self.prev_q
        self.Y_des = []

        self.simulation_time = 0

        self.torque_timer = rospy.Timer(rospy.Duration(self.time_period), self.torque_callback)


    def torque_callback(self, event):
        """
        Sets torque to robot everytime called based on implemented controller.
        """
        
        Y = self.panda_mech.solve_fk(q)
        Y_des = circle_trajectory(self.simulation_time)

        q_des = self.panda_mech.solve_ik(q=q, x=Y_des[0], y=Y_des[1], z=Y_des[2])
        q = np.array(self.arm.angles()) # Angle position in rads
        dq = (q - self.prev_q) / self.time_period # Angular Velocity  of the joints (estimation) # TODO: get velocity directly from joints??
        J = self.panda_mech.get_Jacobian(q)
        
        u = PD(q, dq, q_des)

        self.arm.exec_torque_cmd(list(u))

        self.prev_q = q
        self.simulation_time += self.time_period



if __name__ == '__main__':
    rospy.init_node('TorqueController')
    arm = PandaArm()
    arm.move_to_neutral()

    controller = Simulation(arm)

    rospy.spin()


    # rospy.init_node("panda_demo") # initialise ros node
    