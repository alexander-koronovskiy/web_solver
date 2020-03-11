import re


def put_strings(phrase):
    """
    method for record request phrase to equation record

    :param phrase: request phrase
    :return: list of equation strings
    """
    return phrase.split()


def put_matrix(lines):
    """
    method for record list of equation strings to eq matrix

    :param lines: list of equation strings
    :return: eq matrix
    """
    # lines = phrase.split()

    for i in range(len(lines)):
        if lines[i][0] not in '1234567890+-=':
            lines[i] = '1' + lines[i]

    # нахождение всех чисел - запись в матрицу
    nums = [re.findall(r'\d*\.\d+|\d+', lines[i]) for i in range(len(lines))]
    matrix = [[float(i) for i in line] for line in nums]
    return list(filter(None, matrix))


def solve_linear(matrix):
    pass
