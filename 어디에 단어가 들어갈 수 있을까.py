# SWEA[어디에 단어가 들어갈 수 있을까]

for t in range(int(input())) :
    N, K = map(int, input().split())
    puzzle = [[0]*(N+2) for _ in range(N+2)]
    for i in range(1, N+1) :
        puzzle[i] = [0] + list(map(int, input().split())) + [0]

    row = 0
    for i in range(1, N+1) :
        count = 0
        for j in range(N+1) :
            if puzzle[i][j] == 0 :
                if puzzle[i][j+1] != puzzle[i][j] :
                    count += 1
            else :
                if puzzle[i][j+1] == puzzle[i][j] :
                    count += 1
                else :
                    if count == K :
                        row += 1
                    count = 0

    
    col = 0
    for i in range(1, N+1) :
        count = 0
        for j in range(N+1) :
            if puzzle[j][i] == 0 :
                if puzzle[j+1][i] != puzzle[j][i] :
                    count += 1
            else :
                if puzzle[j+1][i] == puzzle[j][i] :
                    count += 1
                else :
                    if count == K :
                        col += 1
                    count = 0

    print('#%d %d' %(t+1,row+col))
