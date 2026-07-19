# ===================================================
# The function

# current_sales: a list of the current sales of the seats
#                this function does not modify current_sales!
# c_id: 乘客碼
# c_pref: 座位喜好
# s_start: an integer of the starting station
# s_end: an integer of the ending station
def try_to_sell(current_sales, c_id, s_start, s_end):
    # Initialize the return value: success and assigned_seat
    find = False
    seat = []

    for i in range(len(current_sales)): #先看有沒有不用換座的
        successSeat = True
        for j in range(s_start, s_end):
            if current_sales[i][j - 1] != 0:
                successSeat = False
                break
        if successSeat:

            for station in range(s_start - 1, s_end - 1):
                seat.append([i, station])
            return True, seat

    for swapStation in range(s_start, s_end):
        for beforeSeat in range(len(current_sales)): #試每個座位
            # 前半段座位必須都是空位
            ok = True
            for seg in range(s_start - 1, swapStation):
                if current_sales[beforeSeat][seg] != 0: #這個座位這個站有人
                    ok = False
                    break
            if not ok:
                continue

            for afterSeat in range(len(current_sales)):
                if beforeSeat == afterSeat:
                    continue

                # 後半段座位必須都是空位
                ok = True
                for seg in range(swapStation, s_end - 1):
                    if current_sales[afterSeat][seg] != 0:
                        ok = False
                        break
                if not ok:
                    continue

                #加進去
                for seg in range(s_start - 1, swapStation):
                    seat.append([beforeSeat, seg])
                for seg in range(swapStation, s_end - 1):
                    seat.append([afterSeat, seg])

                return True, seat
    return False, seat
# ===================================================


# ===================================================
# The input module

#讀初始資訊
first_line = input().split(',') 
seat_cnt = int(first_line[0])  # 座位
segment_cnt = int(first_line[1])  # 路段
passenger_cnt = int(first_line[2])  # 幾個人

passengers = [] #乘客資訊
passenger_start = input().split(',')
passenger_end = input().split(',')

# 讀每一個乘客資訊
for i in range(passenger_cnt):
    s_start = int(passenger_start[i])  # Starting station
    s_end = int(passenger_end[i])    # Ending station
    passengers.append([s_start, s_end])
# ===================================================


# ===================================================
# The computation module

current_sales = []
for _ in range(seat_cnt):
    one_seat = [0] * segment_cnt #先預設每個路段每個座位都沒人 : 0
    current_sales.append(one_seat)


# Process each passenger's request
for i in range(passenger_cnt):
    s_start, s_end = passengers[i]
    # Try to assign a seat to the passenger
    success, seat = try_to_sell(current_sales, i + 1, s_start, s_end)
    if success: #成功訂票 更新售票系統
        for seat_i in seat:
            current_sales[seat_i[0]][seat_i[1]] = i + 1  # Assign the passenger ID to the seat
# ===================================================


# ===================================================
# The output module
for seat in current_sales:

    for j in range(len(seat)):
        print(seat[j], end='') 
        if j < len(seat) - 1:
            print(',', end='')
    print()
