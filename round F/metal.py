for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]
    inter = []
    
    for i in range(N):
        S, E = [int(x) for x in input().split()]
        inter.append((S, E))
    
    inter.sort()
            
    used = 0
    last = -1
    
    for start, end in inter:
        if last < start:
            last = start + K
            used += 1
        if last < end:
            curr = (K + end - last - 1) // K
            used += curr
            last += curr * K
    
    
    
    print('Case #{}:'.format(tc + 1), used)