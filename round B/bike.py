for tc in range(int(input())):
    N = int(input())
    arr = [int(x) for x in input().split()]
    
    count = 0
    for a, b, c in zip(arr, arr[1:], arr[2:]):
        if a < b > c:
            count += 1
    
    print("Case #{}: {}".format(tc + 1, count))