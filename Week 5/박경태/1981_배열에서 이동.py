def covert_xy(i) :
    return i // 100, i % 100
def covert_int(row, col) :
    return row * 100 + col

def surround(pos, n) :
    a = []
    for p in pos :
        row, col = covert_xy(p)
        if row < n-1 :
            temp = covert_int(row+1, col)
            if temp not in pos :
                a.append(temp)
        if col < n-1 :
            temp = covert_int(row, col+1)
            if temp not in pos :
                a.append(temp)
        if row > 0 :
            temp = covert_int(row-1, col)
            if temp not in pos :
                a.append(temp)
        if col > 0 :
            temp = covert_int(row, col-1)
            if temp not in pos :
                a.append(temp)
    a = list(set(a))
    return a

n = int(input())
maps = [[int(i) for i in input().split()] for j in range(n)]
start = maps[0][0]
pos = [0]
min_n = maps[0][0]
max_n = maps[0][0]
end = covert_int(n-1, n-1)
while True :
    temp_answer = 1000
    temp_c = 1000
    next_pos = surround(pos, n)
    next_row, next_col = 0, 0
    for p in next_pos :
        row, col = covert_xy(p)
        next_step = maps[row][col]
        if min_n < next_step and next_step < max_n :
            pos.append(covert_int(row, col))
            break
        coverage = max(max_n, next_step) - min(min_n, next_step)
        c = abs(next_step - start)
        if temp_answer > coverage :
            temp_answer = coverage
            temp_c = c
            next_row, next_col = row, col
        elif temp_answer == coverage :
            if temp_c > c :
                temp_answer = coverage
                temp_c = c
                next_row, next_col = row, col
    else :
        pos.append(covert_int(next_row, next_col))
        next_num = maps[next_row][next_col]
        max_n, min_n = max(max_n, next_num), min(min_n, next_num)
    
    if end in pos :
        break
    
print(max_n - min_n)