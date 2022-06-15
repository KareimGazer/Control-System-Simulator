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

Tf = 100
Ts = 0.01
y_points = []
x_points = []
I = Integrator(Ts)
for x in np.arange(0, Tf, Ts):
    x_points.append(x)
    y_dash = x + 4
    I.input(y_dash)
    y = I.output()
    y_points.append(y)
plt.plot(x_points, y_points)
plt.show()
