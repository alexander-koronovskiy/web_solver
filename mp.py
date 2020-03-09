import matplotlib.pyplot as plt
import numpy as np


def graph_data():
    x = [0.1*i for i in range(100)]
    y = np.sin(x)
    return y


def plt_data(arr):
    plt.plot(arr)
    plt.savefig('img/fig.png', dpi=100)
    plt.clf()
