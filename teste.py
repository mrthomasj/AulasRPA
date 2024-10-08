def getSequenceSum(i, j, k):
    result = 0
    while i < j:
        i += 1
        result += i
        print(result)
    result += j
    while j > k:
        j -= 1
        result += j
        print(result)
    print(result)


getSequenceSum(-5, -1, -3)