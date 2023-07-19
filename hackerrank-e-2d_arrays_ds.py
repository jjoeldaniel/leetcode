#!/bin/python3

import os

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    s = set()

    for i in range(1, 5):
        for x in range(1, 5):
            s.add(
                arr[i-1][x-1] + arr[i-1][x] + arr[i-1][x+1] +
                arr[i][x] +
                arr[i+1][x-1] + arr[i+1][x] + arr[i+1][x+1]
            )

    return max(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
