N, M, x, y, K = map(int, input().split())
direction = {1:[0, 1], 2:[0, -1], 3:[-1, 0], 4:[1,0]}
maps = []
dice_x = [0, 0, 0, 0]
dice_y = [0, 0, 0, 0]
for i in range(N) :
    maps.append([int(i) for i in input().split()])
    
orders = [int(i) for i in input().split()]
for order in orders :
    mov_x, mov_y = direction[order]
    cor_x, cor_y = x + mov_x, y + mov_y
    if cor_x >= 0 and cor_x < N and cor_y >= 0 and cor_y < M :
        x = cor_x
        y = cor_y
        if mov_x == 0 :
            if mov_y == 1 :
                dice_y = [dice_y[3]] + dice_y[:3]
            else :
                dice_y = dice_y[1:] + [dice_y[0]]
            dice_x[0] = dice_y[0]
            dice_x[2] = dice_y[2]
        else :
            if mov_x == 1:
                dice_x = [dice_x[3]] + dice_x[:3]
            else :
                dice_x = dice_x[1:] + [dice_x[0]]
            dice_y[0] = dice_x[0]
            dice_y[2] = dice_x[2]
            
        if maps[x][y] == 0 :
            maps[x][y] = dice_x[0]
        else :
            dice_x[0] = maps[x][y]
            dice_y[0] = maps[x][y]
            maps[x][y] = 0
            
        print(dice_x[2])
