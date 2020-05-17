squares = set()

for i in range(100000):
    squares.add(i * i)

for tc in range(int(input())):
    N = int(input())
    
    arr = [int(x) for x in input().split()]
    
    pre = [0] 
    for val in arr:
        pre.append(val + pre[-1])
    
    
    count = 0
    
    for l in range(N):
        for r in range(l + 1, N + 1):
            if pre[r] - pre[l] in squares:
                count += 1
    
    print("Case #{}: {}".format(tc + 1, count))
    