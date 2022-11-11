def passable(maps, boundary, n) :
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = [[0, 0]]
    temp = [[0 for _ in range(n)] for _ in range(n)]
    temp[0][0] = 1
    while len(q) >= 1 :
        row, col = q.pop(0)
        if temp[row][col] == 1 :
            for i in range(4) :
                d_row = row + dx[i]
                d_col = col + dy[i]
                if d_row < 0 or d_row > n-1 or d_col < 0 or d_col > n-1 or temp[d_row][d_col] == 1 :
                    continue
                if maps[d_row][d_col] in boundary :
                    temp[d_row][d_col] = 1
                    q.append([d_row, d_col])

        if temp[n-1][n-1] == 1 :
            return True
        
    return False

n = int(input())
maps = [[int(i) for i in input().split()] for j in range(n)]
min_num = min([min(row) for row in maps])
max_num = max([max(row) for row in maps])
start = maps[0][0]
end = maps[n-1][n-1]
l_max = min(start, end)
r_min = max(start, end)
l_min = min_num
r_max = max_num
answer = 300000
left = l_min
right = r_min
while l_min <= left <= l_max and r_min <= right <= r_max :
    boundary = range(left, right+1)
    if passable(maps, boundary, n) :
        answer = min(answer, right-left)
        left += 1
    else :
        right += 1
print(answer)