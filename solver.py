import re, unittest, numpy as np
from collections import Counter


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

    # negative coefficient check
    for i in range(len(fragments) - 1):
        if fragments[i][0] is '-' and len(fragments[i]) == 1:
            fragments[i + 1] = '-' + fragments[i + 1]

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
    if sol_m and eq_m:

        l = ' '.join(eq_m[0])
        for i in set(l) - set('1234567890*+-= '):
            if not Counter(l).get(i) == 1:
                print('exception')

        system = [ext_matrix(eq_m[i]) for i in range(len(eq_m))]
        solution = ext_matrix(sol_m)
        try:
            ans = np.linalg.solve(system, solution)
        except np.linalg.LinAlgError:
            ans = 'cannot solve matrix. Check the description'

    else:
        ans = 'you entered the empty value'
    return ans


def ext_matrix(lines):
    nums = [re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', lines[i]) for i in range(len(lines))]
    matrix0 = np.array(list(filter(None, [[float(i) for i in line] for line in nums])))
    matrix = [i[0] for i in matrix0]
    return matrix

# x + y = -3
# 2x - 5y = 45
