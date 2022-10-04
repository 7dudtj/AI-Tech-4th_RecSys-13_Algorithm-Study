import sys
from collections import defaultdict
from collections import deque
import string

N = int(input())
nums = []
for _ in range(N):
    nums.append(sys.stdin.readline().strip())
K = int(input())

tmp = string.digits + string.ascii_uppercase
num_dict = defaultdict(int)
for num in nums:
    for i in range(len(num)):
        num_dict[num[i]]+=36**(len(num)-i-1)
sorted_dict = sorted(num_dict.items(), key=lambda x:x[1]*(35-tmp.index(x[0])),reverse=True)
character_list = [a[0] for a in sorted_dict[:K]]
new_num = sum([35 * v if a in character_list else tmp.index(a) * v for a, v in sorted_dict])
new_num_que = deque([])
while True:
    new_num_que.appendleft(tmp[new_num % 36])
    new_num = new_num // 36
    if(new_num==0): break
print(("".join(new_num_que)))
