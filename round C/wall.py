from collections import defaultdict

for tc in range(int(input())):
    R, C = [int(x) for x in input().split()]
    
    wall = []
    for i in range(R):
        wall.append(input().strip())
        
    above = defaultdict(set)
    below = defaultdict(set)
    
    for r in range(R):
        for c in range(C):
            el = wall[r][c]
            
            if r > 0:
                if wall[r - 1][c] != el:
                    above[el].add(wall[r - 1][c])
                
            if r < R - 1:
                if wall[r + 1][c] != el:
                    below[el].add(wall[r + 1][c])
                    
            
    candidates = set(wall[-1])
    
    order = []
    placed = set()
    
    while candidates:
        for candidate in list(candidates):
            for other in below[candidate]:
                if other not in placed:
                    candidates.remove(candidate)
                    break
            else:
                order.append(candidate)
                candidates.remove(candidate)
                placed.add(candidate)
                for val in above[candidate]:
                    candidates.add(val)

    if len(order) == len(below):
        print("Case #{}: {}".format(tc + 1, ''.join(order)))
    else:
        print("Case #{}: {}".format(tc + 1, -1))
        
    