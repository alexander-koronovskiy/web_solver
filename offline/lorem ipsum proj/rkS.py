import matplotlib.pyplot as plt


# Equation System func, ε - relation parameter 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.24
# [0.85, 0.9, 0.95, 1.05, 1.1]
eps = 0.05
omega_d = 0.9
def f_x(x):
    return - omega_d*x[1] - x[2]
def f_y(x):
    return omega_d*x[0] + 0.15*x[1]
def f_z(x):
    return 0.2 + x[0]*x[2] - 10*x[2]
def f_u(x):
    return - 0.95*x[4] - x[5] + eps*(x[0] - x[3])
def f_v(x):
    return 0.95*x[3] + 0.15*x[4]
def f_w(x):
    return 0.2 + x[3]*x[4] - 10*x[5]


# Runge Kutta solution
def rKS(x, fx, n, hs):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xk = []
    for i in range(n):
        k1.append(fx[i](x)*hs)
    for i in range(n):
        xk.append(x[i] + k1[i]*0.5)
    for i in range(n):
        k2.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k2[i]*0.5
    for i in range(n):
        k3.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k3[i]
    for i in range(n):
        k4.append(fx[i](xk)*hs)
    for i in range(n):
        x[i] = x[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6
    return x


def solve():
    f = [f_x, f_y, f_z, f_u, f_v, f_w]
    x = [1, 1, 0, 0.1, 0.1, 0.1]
    hs = 0.1
    X =[]; Y=[]; Z=[]; U=[]; V=[]; W=[]
    for i in range(15000):
        x = rKS(x, f, 6, hs)
        X.append(x[0]); Y.append(x[1]); Z.append(x[2])
        U.append(x[3]); V.append(x[4]); W.append(x[5])
    return [X, Y, Z, U, V, W]


# plotting
def plot_f(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z)
    plt.show()


if __name__ == '__main__':
    s = solve()
    plot_f(s[0], s[1], s[2])
