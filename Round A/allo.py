for tc in range(int(input())):
    N, B = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr.sort()
    count = 0
    while count < N and B >= arr[count]:
        B -= arr[count]
        count += 1
    print("Case #{}: {}".format(tc + 1, count))