for tc in range(int(input())):
    s = input().strip()
    
    from collections import deque
    
    stack = deque()
    
    curr = 1
    pos = [1, 1]
    
    direct = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    
    for char in s:
        if char == '(':
            continue
            
        elif char in direct:
            pos[0] += direct[char][0]
            pos[1] += direct[char][1]
            
        elif char == ')':
            oldPos = pos[:]
            last = curr
            
            curr, pos = stack.pop()
            
            pos[0] += oldPos[0] * last
            pos[1] += oldPos[1] * last
            
        
        else:
            stack.append((curr, pos))
            pos = [0, 0] 
            curr = int(char)

    
    print("Case #{}: {} {}".format(tc + 1, 1 + (pos[0] - 1) % (10 ** 9), 1 + (pos[1] - 1) % (10 ** 9)))