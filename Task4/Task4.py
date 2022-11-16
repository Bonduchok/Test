import math
a = []
with open('task4.txt') as f:
    while True:
        line = f.readline().strip()
        if line:
            a.append(int(line.split('\n')[0]))
        if not line:
            break

b = round(sum(a)/len(a))
k = 0
for id, i in enumerate(a):
    while i != b:
        if i<b:
            i += 1
            k += 1
        elif i>b:
            i-=1
            k += 1
        else:
            b[id] = i
print(k)
