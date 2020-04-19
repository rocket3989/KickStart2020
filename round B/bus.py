for tc in range(int(input())):
    N, D = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    
    def simulate(day):
        for bus in arr:
            wait = 0
            if day % bus != 0: 
                wait = bus - (day % bus)
            
            day += wait
            if day > D: return False
        return True
    
    
    l, r = 0, D
    
    while l != r:
        mid = (l + r + 1) // 2
        
        if simulate(mid):
            l = mid
            
        else:
            r = mid - 1
     
    
    print("Case #{}: {}".format(tc + 1, l))
    
    
    