from heapq import heappush, heappop, heapify
def rUp(x, y):
    if x % y != 0:
        return 1 + (x // y)
    return x // y 

for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    
    h = []
    for a, b in zip(arr, arr[1:]):
        h.append((a - b, 1, b - a))
    
    heapify(h)
    
    for i in range(K):
        score, mid, gap = heappop(h)
        
        heappush(h, (-rUp(gap, mid + 1), mid + 1, gap))
    print("Case #{}: {}".format(tc + 1, -h[0][0]))