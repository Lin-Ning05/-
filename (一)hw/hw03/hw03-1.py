info = (input()).split(",")
m = int(info[0])
n = int(info[1])
q = int(info[2])

seat_table = []
for i in range(m):
    seat_table.append(input().split(","))

customer_seat = [] # 紀錄乘客在各路段所坐的座位編號
for i in range(q):
    customer_seat.append([])

for i in range(n):
    for j in range(m):
        customer_id = int(seat_table[j][i])
        if customer_id != 0:
            customer_seat[customer_id - 1].append(j + 1)

change_1 = 0
change_2 = 0
for i in range(q):
    change = 0
    # 比較是否換座位
    for j in range(len(customer_seat[i]) - 1):
        if customer_seat[i][j] != customer_seat[i][j+1]:
            change += 1
    if change == 1:
        change_1 += 1
    elif change == 2:
        change_2 += 1

print(str(change_1) + "," + str(change_2))
