import itertools

dom = []
num = []
lower = []
upper = []
res = 1
out = 0
n, x= input().split()
n = int(n)
x = int(x)

for i in range(0, n):
    x1, x2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    num.append(i)
    lower.append(x1)
    upper.append(x2)
for i in range(0 , x + 1):
    dom.append(0)

for i in range(0, n): 
    for comb in itertools.combinations(num, i + 1):
        for items in comb:
            if upper[items] + 1 > x:
                upper[items] = x
            for j in range(lower[items], upper[items] + 1):
                dom[j] = 1
        
        for j in range(0, x + 1):
            if dom[j] == 0:
                res = 0
            dom[j] = 0
        out = out + res
        res = 1

print(out)
