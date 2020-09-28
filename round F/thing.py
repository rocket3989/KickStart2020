for tc in range(int(input())):
    N, X = [int(x) for x in input().split()]
    arr = list(enumerate([int(x) for x in input().split()], 1))
    
    arr.sort(key=lambda x: (x[1] - 1) // X)
    ans = [x[0] for x in arr]
            
    print('Case #{}:'.format(tc + 1), *ans)