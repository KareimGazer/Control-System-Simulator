from concurrent.futures import process
from deadtime import DeadTime
from differentiator import Differentiator
from integrator import Integrator
import numpy as np
import matplotlib.pyplot as plt
import math


def x(k):
    return k * k


def y(k):
    return k+1


def control_loop(sampling_time=0.01, Tf=20):
    x_points = []
    y_points = []
    K = []
    for k in np.arange(0, Tf, sampling_time):
        K.append(k)
        x_points.append(math.sin(k))
        y_points.append(y(k))

    plt.plot(K, list(zip(y_points, x_points)))
    plt.show()


# control_loop()

# Tf = 100
# Ts = 0.01
# y_points = []
# x_points = []
# I = Integrator(Ts)
# for x in np.arange(0, Tf, Ts):
#     x_points.append(x)
#     y_dash = math.sin(x)
#     I.input(y_dash)
#     y = I.output()
#     y_points.append(y)
# plt.plot(x_points, y_points)
# plt.show()


# Tf = 100
# Ts = 0.01
# y_dash_points = []
# x_points = []
# D = Differentiator(Ts)
# for x in np.arange(0, Tf, Ts):
#     x_points.append(x)
#     y = x + 4
#     D.input(y)
#     y_dash = D.output()
#     y_dash_points.append(y_dash)
# plt.plot(x_points, y_dash_points)
# plt.show()

sampling_time = 0.01
Tf = 100  # final time
Td = 1  # dead time
P = 150
B = 50  # The bias when the error is zero
r = 50.0  # reference
c = 0  # controled variable
m = 0  # manipulated variable
e = 0  # error

dead_time = DeadTime(sampling_time, Td)
process_output = []
reference = []
K = []
for k in np.arange(0, Tf, sampling_time):
    e = r - c
    m = (100/P) * e + B
    dead_time.input(m)
    c = dead_time.outpt()
    process_output.append(c)
    reference.append(r)
    K.append(k)
plt.plot(K, list(zip(reference, process_output)))
plt.show()
