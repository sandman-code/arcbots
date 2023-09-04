import numpy as np


"""
3-wheel omni-bot drive

all units in mm
"""


# angle orientation of the wheels
alpha = np.pi / 3

# radius of wheels
r = 38.1 / 2

# distance of wheel to center of robot frame
d = 15

# complete transformation matrix
H_0 = np.array([[-d, 1, 0], 
                [-d, -1 / 2, -np.sin(alpha)], 
                [-d, -1 / 2, np.sin(alpha)]])



def fk(omega_bz, v_bx, v_by):
    """
    Calculates the angular wheel velocities of the robot 

    Parameters
    ----------
    omega_bz : float
        Angular velocity of the robot
    v_bx : float
        Linear velocity of the robot in the x-direction
    v_by : float
        Linear velocity of the robot in the y-direction

    Raises
    ------
    None

    Returns
    -------
    u : 1x3 ndarray[float]
        A numpy array of the angular velocities of each wheel
    """
    return (1 / r) * np.dot(H_0, np.array([omega_bz, v_bx, v_by]))


def ik(u_1, u_2, u_3):
    """
    Calculates the angular and linear velocities of the robot

    Parameters
    ----------
    u_1 : float
        Angular velocity of wheel 1
    u_2 : float 
        Angular velocity of wheel 2
    u_3 : float 
        Angular velocity of wheel 3

    Raises
    ------
    None

    Returns
    ------
    q_dot : 1x3 ndarray[float]
        The angular, x, and y velcoities of the robot
    """
    
    return np.round(np.dot(np.linalg.inv(H_0), np.array([u_1, u_2, u_3])) * r, 3)
