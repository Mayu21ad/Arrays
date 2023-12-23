import math
import os
import random
import re
import sys

def hourglassSum(arr):
    maxsum = -99
    for i in range(4):
        for j in range(4):
            t = sum(arr[i][j:j+3])
            m = arr[i+1][j+1]
            b = sum(arr[i+2][j:j+3])
            hourglass = t + m + b
            maxsum = max(hourglass, maxsum)
    return maxsum

if __name__ == '__main__':
    # Generate a random 6x6 array
    random_array = [[random.randint(-9, 9) for _ in range(6)] for _ in range(6)]

    # Print the generated array
    print("Generated 6x6 Array:")
    for row in random_array:
        print(row)

    # Find and print the maximum hourglass sum
    result = hourglassSum(random_array)
    print("\nMaximum Hourglass Sum:", result)
