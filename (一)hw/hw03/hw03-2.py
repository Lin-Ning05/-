info = (input()).split(",")
m = int(info[0])
n = int(info[1])
q = int(info[2])

seat = []
fail = []
for i in range(m):
    seat.append([0] * n)

for i in range(1, q + 1):
    order = input().split(",")
    start = int(order[0])
    end = int(order[1])
    has_seat = False
    for j in range(m): 
        empty = True
        
        # 檢查此座位是否在所有路段都為空
        for k in range(start - 1, end - 1):
            if seat[j][k] != 0:
                empty = False
                break

        if empty:
            for k in range(start - 1, end - 1):
                seat[j][k] = i
            has_seat = True
            break
    if not has_seat:
        fail.append(i)

if len(fail) == 0:
    print(0)
else:
    result = ""
    for i in range(len(fail)):
        if i != 0:
            result += ","
        result += str(fail[i]) 
    print(result)
