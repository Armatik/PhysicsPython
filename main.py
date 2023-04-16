from math import pi, cos
import matplotlib.pyplot as plt
import numpy as np
import asyncore

ts = np.linspace(-300, 300, 100000)


def TheSameDirection(A1=5, A2=8, w1=1.2, w2=1.2, theta1=pi, theta2=3 * pi):

    y1, y2 = [], []
    for t in ts:
        y1.append(A1 * cos(w1 * t + theta1))
        y2.append(A2 * cos(w2 * t + theta2))

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


def TheDifferentDirection(A1=5, A2=8, w1=1.2, w2=1.2, theta1=pi, theta2=3 * pi, xlim=[-20, 20], ylim=[-20, 20]):
    x, y = [], []
    for t in ts:
        x.append(A1 * cos(w1 * t + theta1))
        y.append(A2 * cos(w2 * t + theta2))

    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(10)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.plot(x, y)
    plt.show()

#многопоточная работа функции thesomedirection



if __name__ == '__main__':
    #Биение:
    TheSameDirection(w1=4, w2=4.1)
    # Прямая линия:
    TheDifferentDirection(theta2=2*pi)
    # Окружности 3х разных размеров:
    TheDifferentDirection(theta2=1.5*pi, w1=2, w2=2, A1=5, A2=5, theta1=1*pi)

    TheDifferentDirection(theta2=1.5 * pi, w1=2, w2=2, A1=10, A2=10, theta1=1 * pi)

    TheDifferentDirection(theta2=1.5 * pi, w1=2, w2=2, A1=15, A2=15, theta1=1 * pi)
    # Разные частоты и фазы:
    TheDifferentDirection(w1=2,w2=5, xlim=[-10, 10], ylim=[-10, 10])
    # Разные частоты и амплитуды:
    TheDifferentDirection(w1=3,w2=7, xlim=[-10, 10], ylim=[-10, 10])
    # Разные фазы и амплитуды:
    TheDifferentDirection(w1=2,w2=11, xlim=[-10, 10], ylim=[-10, 10])
    # Разные частоты, фазы и амплитуды:
    TheDifferentDirection(w1=7,w2=3, xlim=[-10, 10], ylim=[-10, 10])


    #Набор:
    # Колебания:
    # TheSameDirection(w1=1.2, w2=1.2)
    # Резонанс:
    # TheSameDirection(w1=1.2, w2=1.2, A1=5, A2=5)
    # Разные направления:
    # TheDifferentDirection()
