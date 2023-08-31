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
alpha = np.pi / 3
r = 38.1 / 2
d = 15
H_0 = np.array([[-d, 1, 0], [-d, -1 / 2, -np.sin(alpha)], [-d, -1 / 2, np.sin(alpha)]])
u_b = np.array([0.0, 0.0, 0.1])
u = H_0 * u_b


def fk(omega_bz, v_bx, v_by):
    return (1 / r) * np.dot(H_0, np.array([omega_bz, v_bx, v_by]))


def ik(u_1, u_2, u_3):
    return np.round(np.dot(np.linalg.inv(H_0), np.array([u_1, u_2, u_3])) * r, 3)


print(fk(0, 4.56, 1))
print(ik(0.23937008, -0.16514569, -0.07422439))
