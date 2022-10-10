n, m, x, y, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
directions = [[0,1],[0,-1],[-1,0],[1,0]]
turn = [[0,5,1,2,4,3], [0,2,3,5,4,1], [5,1,0,3,2,4], [2,1,4,3,5,0]]
dice = [0, 0, 0, 0, 0, 0]

commands = list(map(int, input().split()))

for i in commands:
    x += directions[i-1][0]
    y += directions[i-1][1]
    if x < 0 or x >= n or y < 0 or y >= m:
        x -= directions[i-1][0]
        y -= directions[i-1][1]
        continue
    new_dice = [dice[j] for j in turn[i-1]]
    dice = new_dice

    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0
    print(dice[2])
