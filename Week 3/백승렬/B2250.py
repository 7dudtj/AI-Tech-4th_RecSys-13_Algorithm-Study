# https://developerbee.tistory.com/75
import sys
from collections import defaultdict

class Node:
    def __init__(self, value, parent, left, right):
        self.val = value
        self.parent = parent
        self.left = left
        self.right = right
        
position = 0    # horizontal pos
result = defaultdict(list)    # node location by level

def in_order(node, level):
    global position    
    if node.left != -1:
        in_order(tree[node.left], level+1)

    position += 1
    result[level].append(position)

    if node.right != -1:
        in_order(tree[node.right], level+1)

N = int(sys.stdin.readline())
tree = dict()

# initialize
for i in range(1, N+1):
    tree[i] = Node(i, -1, -1, -1)

# input 
for _ in range(N):
    root, left, right = map(int, sys.stdin.readline().split())
    
    if left != -1:
        tree[root].left = left
        tree[left].parent = root
    if right != -1:
        tree[root].right = right
        tree[right].parent = root

# find root
root = 1
for i in range(1, N+1):
    if tree[i].parent == -1:
        root = tree[i].val


in_order(tree[root], 1)

width = (0,0)

for i in range(1,len(result)+1):
    w = result[i][-1] - result[i][0] + 1
    if w > width[1]:
        width = (i, w)

print(*width)
