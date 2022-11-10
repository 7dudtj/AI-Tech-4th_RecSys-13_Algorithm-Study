def passable(maps, n) :
    start = [0]
    route = [0]
    while True :
        temp = []
        movable = False
        for s in start :
            row, col = s // 100, s % 100
            if maps[row][col] == 1 :
                if row > 0 and maps[row-1][col] == 1 :
                    num = (row-1)*100+col
                    if num not in route :
                        temp.append(num)
                    movable = True
                if row < n-1 and maps[row+1][col] == 1 :
                    num = (row+1)*100+col
                    if num not in route :
                        temp.append(num)
                    movable = True
                if col > 0 and maps[row][col-1] == 1 :
                    num = row*100+col-1
                    if num not in route :
                        temp.append(num)
                    movable = True
                if col < n-1 and maps[row][col+1] == 1 :
                    num = row*100+col+1
                    if num not in route :
                        temp.append(num)
                    movable = True

        if (n-1)*100 + n-1 in route :
            return True

        if not movable :
            return False

        route.extend(temp)
        start = temp

n = int(input())
maps = [[int(i) for i in input().split()] for j in range(n)]
min_num = min([min(row) for row in maps])
max_num = max([max(row) for row in maps])
length = max_num - min_num
start_num = maps[0][0]
end_num = maps[n-1][n-1]
for i in range(abs(start_num - end_num), length+1) :
    for j in range(min(i, start_num - min_num)+1) :
        top = i - j
        boundary = range(start_num-j, start_num+top+1)
        temp = [[1 if i in boundary else 0 for i in row]for row in maps]
        if temp[n-1][n-1] == 0 :
            continue

        if passable(temp, n) :
            print(i)
            break
    else :
        continue

    break