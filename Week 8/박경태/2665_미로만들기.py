n = int(input())
maps = [[int(i) for i in list(input())] for j in range(n)]
boundary = [[0 for i in range(n)] for j in range(n)]
boundary[0][0] = 1
count = 0
while True :
    while True :
        movable = False
        for row in range(n) :
            for col in range(n) :
                if boundary[row][col] == 1 :
                    if row > 0 and (maps[row-1][col] + boundary[row-1][col]) == 1 :
                        boundary[row-1][col] = 1
                        movable = True
                    if row < n-1 and (maps[row+1][col] + boundary[row+1][col]) == 1 :
                        boundary[row+1][col] = 1
                        movable = True

                    if col > 0 and (maps[row][col-1] + boundary[row][col-1]) == 1 :
                        boundary[row][col-1] = 1
                        movable = True
                    if col < n-1 and (maps[row][col+1] + boundary[row][col+1]) == 1 :
                        boundary[row][col+1] = 1
                        movable = True
        if not movable :
            break

    if boundary[n-1][n-1] == 1 :
        break

    for row in range(n) :
        for col in range(n) :
            if boundary[row][col] == 1 :
                if row > 0 and maps[row-1][col] == 0 :
                    maps[row-1][col] = 1
                if row < n-1 and maps[row+1][col] == 0 :
                    maps[row+1][col] = 1

                if col > 0 and maps[row][col-1] == 0 :
                    maps[row][col-1] = 1
                if col < n-1 and maps[row][col+1] == 0 :
                    maps[row][col+1] = 1

    count += 1
print(count)