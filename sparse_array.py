import os

def matchingStrings(stringList, queries):
    s = {} 
    for string in stringList:
        s[string] = s.get(string, 0) + 1  

    result = []
    for q in queries:
        result.append(s.get(q, 0)) 
    return result

if __name__ == '__main__':
    stringList_count = int(input().strip())
    stringList = [input().strip() for _ in range(stringList_count)]

    queries_count = int(input().strip())
    queries = [input().strip() for _ in range(queries_count)]

    res = matchingStrings(stringList, queries)

    print('\n'.join(map(str, res)))
