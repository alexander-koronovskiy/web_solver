import numpy as np
# import matplotlib.pyplot as plt


def test_sin():
    # argument list forming (cycle "for" used)
    x = [0.1*i for i in range(100)]

    # function list forming by numpy method - sin()
    y = np.sin(x)

    # plotting function
    return y
