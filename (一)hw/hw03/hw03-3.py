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
    can_book = False

    # 全程坐同一個座位
    for j in range(m): 
        empty = True
        for k in range(start - 1, end - 1):
            if seat[j][k] != 0:
                empty = False
                break
        if empty:
            for k in range(start - 1, end - 1):
                seat[j][k] = i
            has_seat = True
            break

    # 每段換座位
    if not has_seat:
        temp = []
        can_book = True
        for j in range(start - 1, end - 1):
            found = False
            for k in range(m):
                if seat[k][j] == 0:
                    seat[k][j] = i
                    temp.append([k, j])
                    found = True
                    break

            # 某段沒有空位就取消之前路段安排的座位
            if not found: 
                can_book = False
                for k in range(len(temp)):
                    seat[temp[k][0]][temp[k][1]] = 0
                break
        
    if can_book:
        has_seat = True
        
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
