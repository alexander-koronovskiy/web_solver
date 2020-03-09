import re


def put_strings(phrase):
    """
    method for record request phrase to equation record

    :param phrase: request phrase
    :return: list of equation strings
    """
    start = -1
    lines = []
    for i in range(len(phrase)):
        if phrase[i] == '\n':
            lines.append(phrase[start+1:i-1])
            start = i
    lines.append(phrase[start + 1:len(phrase)])
    for i in lines:
        if (i == '\r') and (i.isEmpty()):
            lines.remove(i)
    return lines


def put_matrix(lines):
    """
    method for record list of equation strings to eq matrix
    :param lines: list of equation strings
    :return: eq matrix
    """
    nums = [re.findall(r'\d*\.\d+|\d+', lines[i]) for i in range(len(lines))]
    return nums
