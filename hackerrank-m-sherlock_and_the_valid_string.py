#!/bin/python3

import os
from collections import defaultdict

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    d = defaultdict(int)  # char: freq
    x = defaultdict(list)  # freq, list of chars

    # initialize maps
    for i in s:
        d[i] += 1
    for k, v in d.items():
        x[v].append(k)

    # if three or more frequencies exist
    if len(x.keys()) > 2:
        return "NO"
    # if there exists only one frequency
    elif len(x.keys()) == 1:
        return "YES"

    outliers = []
    # check if more than one outlier char
    for k, v in x.items():

        # we now know there are only 2 keys
        # return NO if the value for BOTH
        # is greater than 2 (implies more than one
        # outlier)
        if len(v) > 2:
            outliers.append(True)
        else:
            outliers.append(False)

    if outliers[0] and outliers[1]:
        return "NO"

    # outlier check
    freq = None
    found_outlier = False
    for k, v in d.items():
        if freq and freq != v:
            if (not found_outlier) and v == 1 or freq == v-1:
                found_outlier = True
                continue
            else:
                return "NO"
        freq = v

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
