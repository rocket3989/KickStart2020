from heapq import heappush, heappop, heapify


for tc in range(int(input())):
    N, K, P = [int(x) for x in input().split()]
    stacks = []
    pres = []
    
    for i in range(N):
        stacks.append([int(x) for x in input().split()])
        pre = [0]
        for val in stacks[-1]:
            pre.append(pre[-1] + val)
        pres.append(pre)
    print(pres)
    starts = [0] * N
    score = 0
    
    def test(s, pos):
        b = starts[s]
        print(pos, b)
        if pos < b: return 0
        return (pres[s][pos] - pres[s][b]) / (pos - b)
    h = []
    
    for i, stack in enumerate(stacks):
        s, c = 0, 0
        for val in stack[:P]:
            s += val
            c += 1
            h.append((-s / c, i, c))
    
    heapify(h)
    
    
    while P:
        print(h)
        curr, s, pos = heappop(h)
        curr = -curr
        newScore = test(s, pos)
        
        if pos > P + starts[s]: continue
        
        if curr != newScore:
            heappush(h, (-newScore, s, pos))
            continue
        
        
        for val in stacks[s][starts[s] : pos]:
            score += val
        
        P -= pos - starts[s] 
        starts[s] = pos
        
    print("Case #{}: {}".format(tc + 1, score))
