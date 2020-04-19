for tc in range(int(input())):
    W, H, L, U, R, D = [int(x) for x in input().split()]
    
    L -= 1
    U -= 1
    R -= 1
    D -= 1
    
    
    
    
    dp = [[0 for i in range(W)] for j in range(H)]
    
    dp[0][0] = 1
    
    for r in range(H):
        for c in range(W):
            if L <= c <= R and U <= r <= D:
                continue
            
            if c == W - 1 and r == H - 1:
                continue
                
            if c == W - 1:
                dp[r + 1][c] += dp[r][c]
           
            elif r == H - 1:
                dp[r][c + 1] += dp[r][c]
            
            else:
                dp[r][c + 1] += dp[r][c] * .5
                dp[r + 1][c] += dp[r][c] * .5
    
    # for row in dp:
    #     print(*row)
    
    print("Case #{}: {}".format(tc + 1, dp[-1][-1]))
