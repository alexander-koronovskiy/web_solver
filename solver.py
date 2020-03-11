import re, numpy as np


def put_matrix(phrase):
    """
    method for solution eq matrix by eq phrase

    :param phrase: equation phrase
    :return: eq matrix solution
    """
    # separation
    fragments = phrase.split()

    # add unit coefficient
    for i in range(len(fragments)):
        if fragments[i][0] not in '1234567890*+-=':
            fragments[i] = '1' + fragments[i]

    # matrix fragmentation
    eq_m = []
    sol_m = []
    nl = -2
    for i in range(len(fragments)):
        if fragments[i] is '=':
            eq_m.append(fragments[nl+2:i])
            sol_m.append(fragments[i + 1])
            nl = i

    # solution
    system = [ext_matrix(eq_m[i]) for i in range(len(eq_m))]
    solution = ext_matrix(sol_m)
    ans = np.linalg.solve(system, solution)
    return ans


def ext_matrix(lines):
    nums = [re.findall(r'\d*\.\d+|\d+', lines[i]) for i in range(len(lines))]
    matrix0 = np.array(list(filter(None, [[float(i) for i in line] for line in nums])))
    matrix = [i[0] for i in matrix0]
    return matrix
