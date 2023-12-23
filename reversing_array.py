def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    arr = list(map(int, input("Enter space-separated integers: ").split()))

    res = reverseArray(arr)

    print("Reversed Array:", res)
