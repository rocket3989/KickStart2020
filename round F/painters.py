for tc in range(int(input())):
    S, R1, P1, R2, P2, C = [int(x) for x in input().split()]
    
    blocked = set(((R1, P1), (R2, P2)))
    
    for i in range(C):
        r, p = [int(x) for x in input().split()]
        blocked.add((r, p))
    
    def search(stale, turn, blocked, score, length, R1, P1, R2, P2):
        # print(blocked)
        if stale > 1:
            return score
        if turn == 0: #alma, 0
            best = -1000
            if P1 > 1 and (R1, P1 - 1) not in blocked:
                blocked.add((R1, P1 - 1))
                best = search(0, 1, blocked, score + 1, length, R1, P1 - 1, R2, P2)
                blocked.remove((R1, P1 - 1))
                
            if P1 < 2 * R1 - 1 and (R1, P1 + 1) not in blocked:
                blocked.add((R1, P1 + 1))
                best = max(best, search(0, 1, blocked, score + 1, length, R1, P1 + 1, R2, P2))
                blocked.remove((R1, P1 + 1))
                
            if P1 & 1 and R1 < length and (R1 + 1, P1 + 1) not in blocked:
                blocked.add((R1 + 1, P1 + 1))
                best = max(best, search(0, 1, blocked, score + 1, length, R1 + 1, P1 + 1, R2, P2))
                blocked.remove((R1 + 1, P1 + 1))
            
            if P1 & 1 == 0 and (R1 - 1, P1 - 1) not in blocked:
                blocked.add((R1 - 1, P1 - 1))
                best = max(best, search(0, 1, blocked, score + 1, length, R1 - 1, P1 - 1, R2, P2))
                blocked.remove((R1 - 1, P1 - 1))
            
            
            if best == -1000:
                best = max(best, search(stale + 1, 1, blocked, score, length, R1, P1, R2, P2))
            
            return best
        
        else:
            best = 1000
            if P2 > 1 and (R2, P2 - 1) not in blocked:
                blocked.add((R2, P2 - 1))
                best = search(0, 0, blocked, score - 1, length, R1, P1, R2, P2 - 1)
                blocked.remove((R2, P2 - 1))
                
            if P2 < 2 * R2 - 1 and (R2, P2 + 1) not in blocked:
                blocked.add((R2, P2 + 1))
                best = min(best, search(0, 0, blocked, score - 1, length, R1, P1, R2, P2 + 1))
                blocked.remove((R2, P2 + 1))
            
            if P2 & 1 and R2 < length and (R2 + 1, P2 + 1) not in blocked:
                blocked.add((R2 + 1, P2 + 1))
                best = min(best, search(0, 0, blocked, score - 1, length, R1, P1, R2 + 1, P2 + 1))
                blocked.remove((R2 + 1, P2 + 1))
                
            if P2 & 1 == 0 and (R2 - 1, P2 - 1) not in blocked:
                blocked.add((R2 - 1, P2 - 1))
                best = min(best, search(0, 0, blocked, score - 1, length, R1, P1, R2 - 1, P2 - 1))
                blocked.remove((R2 - 1, P2 - 1))
            
    
            
            if best == 1000:
                best = search(stale + 1, 0, blocked, score, length, R1, P1, R2, P2)
            return best
            
    print('Case #{}:'.format(tc + 1), search(0, 0, blocked, 0, S, R1, P1, R2, P2))
    