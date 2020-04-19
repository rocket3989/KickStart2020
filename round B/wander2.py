def choose(n, k):

    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0




for tc in range(int(input())):
    W, H, L, U, R, D = [int(x) for x in input().split()]
    
    L -= 1
    U -= 1
    R -= 1
    D -= 1
    
    ans = 0
    # top path
    
    if R + 1 < W and U > 0:
        dist = R + 1
        height = U
        
        count = height - 1
        print(height, dist)
        for i in range(height):
            count += choose(i, dist)
            print(i, dist, choose(i, dist))
        
        ans = count * (.5) ** (dist + height - 1)
        
    #left path
    
    if D + 1 < H and L > 0:
        dist = D + 1
        height = L

        count = height - 1
        for i in range(height):
            count += choose(dist, i)

        ans += count * (.5) ** (dist + height - 1)
    
        print(count, dist + height - 1)
        

    print("Case #{}: {}".format(tc + 1, ans))
    