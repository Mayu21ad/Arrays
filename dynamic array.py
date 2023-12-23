def dynamicArray(n, queries):
    # Initialize a list of empty sequences (lists)
    seq = [[] for _ in range(n)]
    # Initialize the variable to store the last answer
    lastanswer = 0
    # Initialize a list to store the results of queries of type 2
    result = []

    # Iterate through each query
    for q, x, y in queries:
        # If the query is of type 1
        if q == 1:
            # Calculate the index based on XOR of x and lastanswer
            idx = (x ^ lastanswer) % n
            # Append y to the corresponding sequence
            seq[idx].append(y)
        # If the query is of type 2
        else:
            # Calculate the index based on XOR of x and lastanswer
            idx = (x ^ lastanswer) % n
            # Calculate the value of v
            v = y % len(seq[idx])
            # Update lastanswer with the value at index v in the sequence
            lastanswer = seq[idx][v]
            # Append lastanswer to the result list
            result.append(lastanswer)

    # Return the list of results for queries of type 2
    return result

if __name__ == '__main__':
    # Read input values
    n, q = map(int, input().rstrip().split())

    queries = []

    # Read each query and append it to the list of queries
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    # Call the dynamicArray function and store the result
    result = dynamicArray(n, queries)

    # Print the results
    print('\n'.join(map(str, result)))
