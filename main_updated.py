
from PandaMechanics import PandaMechanics
from trajectory import circle_trajectory
from controller_updated import CLF_QP_with_error
import numpy as np
import pybullet as p
import pybullet_data
import time

def run_simulation():
    """
    Runs the simulation with CLF-QP controller and Z-force handling.
    """
    panda_mech = PandaMechanics()
    simulation_time = 0
    JOINTS = [i for i in range(p.getNumJoints(robot) - 1)]

    while True:
        # Desired trajectory
        Y_des = circle_trajectory(simulation_time)
        q_des = panda_mech.solve_ik(q=q, x=Y_des[0], y=Y_des[1], z=Y_des[2])

        # Current state
        q = np.array([p.getJointState(robot, i)[0] for i in JOINTS])
        dq = np.array([p.getJointState(robot, i)[1] for i in JOINTS])
        
        # Jacobian computation
        J = panda_mech.get_Jacobian(q)

        # Force and control
        Fz = 1.0  # Desired force in the Z direction
        u = CLF_QP_with_error(q, dq, q_des, dq_des=np.zeros_like(q), ddq_des=np.zeros_like(q), Fz=Fz, J=J)

        # Apply control torques
        p.setJointMotorControlArray(
            bodyIndex=robot,
            jointIndices=JOINTS,
            controlMode=p.TORQUE_CONTROL,
            forces=u
        )

        # Step simulation
        p.stepSimulation()
        simulation_time += 1 / 240
        time.sleep(1 / 240)

# Simulation setup (initialization, loading URDFs, etc.) remains unchanged.
