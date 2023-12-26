
def arrayManipulation(n, queries):
    arr = [0] * (n+2)
    for a, b, k in queries:
        arr[a] += k
        arr[b+1] -= k

    maxsum = temp = 0
    for val in arr:
        temp += val
        maxsum = max(maxsum, temp)
    return maxsum

n = 5
queries = [
    (1, 2, 100),
    (2, 5, 200),
    (3, 4, 150)
]

result = arrayManipulation(n, queries)

print("Maximum value after array manipulation:", result)
