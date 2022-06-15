import numpy as np
import matplotlib.pyplot as plt


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
        x_points.append(x(k))
        y_points.append(y(k))

    plt.plot(K, list(zip(y_points, x_points)))
    plt.show()


control_loop()
