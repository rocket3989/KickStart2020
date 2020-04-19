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
    
    if W - 1 == R - L or H - 1 == U - D:
        print("Case #{}: {}".format(tc + 1, 0))
        continue
    
    ans = 1
    # top path
    
    
    if U > 0:
        for c in range(L, R + 1):
            if c == W - 1:
                
                for r in range(U):
                    ans -= choose(c + r - 1, r) * (.5) ** (c + r - 1) 
                
                
            else:          
                ans -= choose(c + U - 1, c) * (.5) ** (c + U)
                
    #left path
    if L > 0:
        for r in range(U, D + 1):
            print(r)
            if r == H - 1:
                for c in range(L):
                    ans -= choose(c + r - 1, c) * (.5) ** (c + r - 1)
            
            else:
                ans -= choose(r + U - 1, r) * (.5) ** (r + U)
            
        

    print("Case #{}: {}".format(tc + 1, ans))