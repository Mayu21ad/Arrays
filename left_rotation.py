def rotateLeft(d, arr):
    arr = arr[d:] + arr[:d]
    return arr

if __name__ == '__main__':
    input_array = [1, 2, 3, 4, 5]

    rotations = 2

    result = rotateLeft(rotations, input_array)

    print(f"Original Array: {input_array}")
    print(f"Array after {rotations} left rotations: {result}")
