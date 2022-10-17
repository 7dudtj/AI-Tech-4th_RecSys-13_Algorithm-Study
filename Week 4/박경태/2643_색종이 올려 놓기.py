count = int(input())
data = []
for i in range(count) :
    w, h = map(int, input().split())
    data.append([min(w, h), max(w, h)])
data.sort()

p_w, p_h = data[0]
stack = [1 for _ in range(count)]
for i, (w, h) in enumerate(data) :
    for j in range(i) :
        p_w, p_h = data[j]
        if p_w <= w and p_h <= h :
            stack[i] = max(stack[i], stack[j] + 1)
            
print(max(stack))
