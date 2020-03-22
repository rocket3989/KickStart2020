for tc in range(int(input())):
    N, K, P = [int(x) for x in input().split()]
    stacks = []
    pres = []
    
    for i in range(N):
        stacks.append([int(x) for x in input().split()])
    
    memo = {}
    def recur(s, rem):
        if s >= N: return 0
        if (s, rem) in memo:
            return memo[(s, rem)]
        best = recur(s + 1, rem)
        curr = 0
        for i, val in enumerate(stacks[s][:rem]):
            curr += val
            best = max(best, curr + recur(s + 1, rem - i - 1))
        memo[(s,rem)] = best
        return best
    
    print("Case #{}: {}".format(tc + 1, recur(0, P)))
    