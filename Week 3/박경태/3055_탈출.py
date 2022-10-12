def pos(R, C, row, col) :
    positions = []
    if row > 0 :
        positions.append([row-1, col])
    if row < R-1 :
        positions.append([row+1, col])

    if col > 0 :
        positions.append([row, col-1])
    if col < C-1 :
        positions.append([row, col+1])

    return positions
        

R, C = map(int, input().split())
maps = []
D = []
X = []
W = []
S = []
for r in range(R) :
    data = list(input())
    for c, item in enumerate(data) :
        if item == 'D' :
            D = [r, c]
        elif item == 'X' :
            X.append([r, c])
        elif item == '*' :
            W.append([r, c])
        elif item == 'S' :
            S.append([r, c])

    maps.append(data)
    
answer = 1
while True :
    for s in S :
        for r, c in pos(R, C, s[0], s[1]) :
            maps[r][c] = 'S'

    for w in W :
        for r, c in pos(R, C, w[0], w[1]) :
            if [r, c] == D :
                continue
            maps[r][c] = '*'
        
    for r, c in X :
        maps[r][c] = 'x'
    
    if maps[D[0]][D[1]] == 'S' :
        print(answer)
        break
    
    maps[D[0]][D[1]] = 'D'
    s_temp = []
    w_temp = []
    for r, row in enumerate(maps) :
        for c, item in enumerate(row) :
            if item == 'S' :
                s_temp.append([r, c])
            elif item == '*' :
                w_temp.append([r, c])
    
    if len(s_temp) == 0 :
        print('KAKTUS')
        break
    
    S = s_temp
    W = w_temp
    
    answer += 1
