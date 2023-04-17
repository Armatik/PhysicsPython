from math import pi, cos, sin
import matplotlib.pyplot as plt
import numpy as np

ts = np.linspace(-300, 300, 100000)


def TheSameDirection(A1=5, A2=8, f1=1.2, f2=1.2, theta1=pi, theta2=3 * pi):

    y1, y2 = [], []
    for t in ts:
        y1.append(A1 * cos(f1 * t + theta1))
        y2.append(A2 * cos(f2 * t + theta2))

    fig = plt.figure()
    #fig.set_figheight(3)
    #fig.set_figwidth(3)
    plt.xlim([-100, 100])
    plt.ylim([-25, 25])
    #plt.plot(ts, y1, alpha=0.5, c='deeppink')
    #plt.plot(ts, y2, alpha=0.5, c='blue')
    y = []
    for i in range(len(y1)):
        y.append(y1[i] + y2[i])
    plt.plot(ts, y, c='red', alpha=0.5)
    plt.show()


def TheDifferentDirection(A1=5, A2=8, f1=1.2, f2=1.2, theta1=pi, theta2=3 * pi, xlim=[-20, 20], ylim=[-20, 20]):
    x, y = [], []
    for t in ts:
        x.append(A1 * cos(f1 * t + theta1))
        y.append(A2 * sin(f2 * t + theta2))

    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(10)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    #Биение:
    TheSameDirection(f1=4, f2=4.1)
    # Прямая линия:
    TheDifferentDirection(f1=10, f2=10, xlim=[-2, 2], ylim=[-2, 2], A1=1, A2=1, theta1=1.5*pi, theta2=pi)
    # Отзеркаленая прямая линия:
    TheDifferentDirection(f1=10, f2=10, xlim=[-2, 2], ylim=[-2, 2], A1=1, A2=1, theta1=pi, theta2=1.5*pi)
    # Окружности 3х разных размеров:
    TheDifferentDirection(f1=10, f2=10, xlim=[-2, 2], ylim=[-2, 2], A1=0.5, A2=0.5, theta1=pi, theta2=pi)

    TheDifferentDirection(f1=10, f2=10, xlim=[-2, 2], ylim=[-2, 2], A1=1, A2=1, theta1=pi, theta2=pi)

    TheDifferentDirection(f1=10, f2=10, xlim=[-2, 2], ylim=[-2, 2], A1=1.5, A2=1.5, theta1=pi, theta2=pi)


    # рис 6
    TheDifferentDirection(f1=30, f2=20, xlim=[-2, 2], ylim=[-2, 2], A1=1, A2=1, theta1=pi, theta2=pi)
    # Рис 7
    TheDifferentDirection(f1=40, f2=20, xlim=[-2, 2], ylim=[-2, 2], A1=1, A2=1, theta1=0.5 * pi, theta2=pi)
    # Рис 8:
    TheDifferentDirection(f1=60, f2=20, xlim=[-2, 2], ylim=[-2, 2], A1=1, A2=1, theta1=0.5 * pi, theta2=pi)
    # Рис 9:
    TheDifferentDirection(f1=20, f2=30, xlim=[-2, 2], ylim=[-2, 2], A1=1, A2=1, theta1=0.5 * pi, theta2=pi)

