r = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

m = int(input())
n = int(input())

count = 0
for x in range(m + 1):
    for y in range(n + 1):
        if (abs(x - x1) + abs(y - y1) > r and 
            abs(x - x2) + abs(y - y2) > r and 
            abs(x - x3) + abs(y - y3) > r):
            count += 1
print(count)
