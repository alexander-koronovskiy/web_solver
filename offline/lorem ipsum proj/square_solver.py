import cmath


def square_solve(a, b, c):
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return sol1, sol2


sol = square_solve(1, 1, -2)
print('{0} {1}'.format(sol[0], sol[1]))
