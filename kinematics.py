"""

Linear direction of the ball is only thing needed

"""


import numpy as np

# translation of ball
x_s = 0
y_s = 0

# orientation of body
phi_x = 0
phi_y = 0
phi_z = 0


q = np.array([x_s, y_s, phi_x, phi_y, phi_z])

# potentially need homo frames

# twist of ball
# velocities of ball
xdot_s = 0
ydot_s = 0

v_2 = np.array([xdot_s, ydot_s, 0])


# Omni-wheel calculations
alpha = np.pi / 4
radius = 20

r_w1 = radius * np.array([np.sin(alpha), 0, np.cos(alpha)])
r_w2 = radius * np.array(
    [-1 / 2 * np.sin(alpha), 1 / 2 * np.sqrt(3) * np.sin(alpha), np.cos(alpha)]
)
r_w3 = radius * np.array(
    [-1 / 2 * np.sin(alpha), -1 / 2 * np.sqrt(3) * np.sin(alpha), np.cos(alpha)]
)

u_w1 = np.array([0, 1, 0])
u_w2 = np.array([-1 / 2 * np.sqrt(3), -1 / 2, 0])
u_w3 = np.array([1 / 2 * np.array(3), -1 / 2, 0])

omega_s = 0
# print(q)


"""
3-wheel omni-bot drive

all units in mm
"""
r = 38.1 / 2
d = 15
H_0 = np.array(
    [[-d, 1, 0], [-d, -1 / 2, -np.sin(np.pi / 3)], [-d, -1 / 2, np.sin(np.pi / 3)]]
)
u_b = np.array([0.0, 0.0, 0.1])
u = H_0 * u_b


def ik(omega_bz, v_bx, v_by):
    return (1 / r) * np.dot(H_0, np.array([omega_bz, v_bx, v_by]))


def fk(u_1, u_2, u_3):
    mat = np.eye(3)
    mat[0, 2] = u_1
    mat[1, 2] = u_2
    mat[2, 2] = u_3
    mat = mat * r
    print(mat)
    return np.linalg.inv(mat) * H_0


print(ik(0, 1, 0))
print(fk(0.05249344, -0.02624672, -0.02624672))
