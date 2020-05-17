for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]
    
    arr = [int(x) for x in input().split()]
    
    last = -1
    series = False
    count = 0
    
    for val in arr:
        if val == K:
            series = True
        
        elif series and val == last - 1:
            if val == 1:
                count += 1
                series = False    
        
        else:
            series = False
    
        last = val
    
    
    
    
    print("Case #{}: {}".format(tc + 1, count))