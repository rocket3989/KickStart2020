
from collections import defaultdict

class node:
    def __init__(self):
        self.childDict = defaultdict(node)
        self.count = 0
    def __str__(self):
        ret = str(self.count) + '\n'
        for k, v in self.childDict.items():
            temp = str(v)
            new = ''
            for val in temp.split('\n'):
                new += '  ' + val + '\n'
            ret += k + ' ' + new + ' '
        return ret
        


for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]
    root = node()
    for i in range(N):
        curr = root
        for char in input().strip():
            curr = curr.childDict[char]
            curr.count += 1
    # print(str(root))
    score = 0
    root.count = N
    def dfs(d, curr):
        dest = 0
        score = 0
        for k, v in curr.childDict.items():
            if v.count >= K:
                score += dfs(d + 1, v)
                dest += (v.count // K) * K 
        score += ((curr.count - dest) // K) * d
        return score
    
    print("Case #{}: {}".format(tc + 1, dfs(0, root)))