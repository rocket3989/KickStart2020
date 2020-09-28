for tc in range(int(input())):
    N = int(input())
    arr = [int(x) for x in input().split()]
    
    length = 1
    lastDiff = float('inf')
    bestlength = 0
    
    for a, b in zip(arr, arr[1:]):
        if b - a == lastDiff:
            length += 1
            
        else:
            bestlength = max(bestlength, length)
            
            length = 2
            lastDiff = b - a
            
    bestlength = max(bestlength, length)
    print("Case #{}: {}".format(tc + 1, bestlength))
    