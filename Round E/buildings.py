for tc in range(int(input())):
    print("Case #{}: ".format(tc + 1), end='')
    
    N, A, B, C = [int(x) for x in input().split()]
    
    
    Abuild = A - C
    Bbuild = B - C
    trash = N - C - Abuild - Bbuild
    
    if Abuild < 0 or Bbuild < 0 or trash < 0:
        print("IMPOSSIBLE")
        continue
    
    ans = []
    if Abuild > 0:
        ans = ([2] * Abuild) + ([1] * trash) + ([3] * C) + ([2] * Bbuild)
    
    elif Bbuild > 0:
        ans = ([3] * C) + ([1] * trash) + ([2] * Bbuild)   
    
    elif C < N:
        ans = [2] + ([1] * trash) + ([2] * (C - 1)) 
        
    else:
        ans = [1] * N
        
    print(*ans)
    
    
    
    