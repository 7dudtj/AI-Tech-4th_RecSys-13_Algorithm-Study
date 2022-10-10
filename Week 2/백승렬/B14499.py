import sys
from collections import deque

N, M, x, y, K = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
comms = list(map(int, sys.stdin.readline().split()))

dice_v = deque([0, 0, 0, 0])
dice_h = deque([0, 0, 0])

# 1:동, 2:서, 3:북, 4:남
dir = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}


def dice_rotate(d):
    if d == 1:
        dice_v[1] = dice_h[0]
        temp = dice_v.pop()
        dice_h.appendleft(temp)
        dice_v.append(dice_h.pop())

    elif d == 2:
        dice_v[1] = dice_h[2]
        temp = dice_v.pop()
        dice_h.append(temp)
        dice_v.append(dice_h.popleft())

    elif d == 3:
        dice_v.rotate(-1)
        dice_h[1] = dice_v[1]

    else:
        dice_v.rotate(1)
        dice_h[1] = dice_v[1]

for n in comms:
    a, b = dir[n]
    next_x, next_y = x + a, y + b

    if 0 <= next_x < N and 0 <= next_y < M:
        dice_rotate(n)
        if board[next_x][next_y]:
            dice_v[3] = board[next_x][next_y]
            board[next_x][next_y] = 0
        else:
            board[next_x][next_y] = dice_v[3]

        x, y = next_x, next_y

        print(dice_v[1])
