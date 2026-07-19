# ===================================================
# The function

# current_sales: a list of the current sales of the seats
#                this function does not modify current_sales!
# c_id: 乘客碼
# c_pref: 座位喜好
# s_start: an integer of the starting station
# s_end: an integer of the ending station
def try_to_sell(current_sales, c_id, c_pref, s_start, s_end):
    # Initialize the return value: success and assigned_seat
    success = False
    assigned_seat = 0  # Set assigned_seat to 0 as default

    if c_pref == 0:
        for i in range(len(current_sales)):
            successSeat = True
            for j in range(s_start, s_end):
                if current_sales[i][j - 1] != 0:
                    successSeat = False
                    break
            if successSeat:
                success = True
                assigned_seat = i + 1 #他是座位123...我是格數012...
                break
    elif c_pref == 1: #先看奇數位
        for i in range(0, len(current_sales), 2):
            successSeat = True
            for j in range(s_start, s_end):
                if current_sales[i][j - 1] != 0:
                    successSeat = False
                    break
            if successSeat:
                success = True
                assigned_seat = i + 1 #他是座位123...我是格數012...
                break
        if not success:
            for i in range(1, len(current_sales), 2):
                successSeat = True
                for j in range(s_start, s_end):
                    if current_sales[i][j - 1] != 0:
                        successSeat = False
                        break
                if successSeat:
                    success = True
                    assigned_seat = i + 1 #他是座位123...我是格數012...
                    break
    else:
        successSeat = True
        for i in range(1, len(current_sales), 2):
            successSeat = True
            for j in range(s_start, s_end):
                if current_sales[i][j - 1] != 0:
                    successSeat = False
                    break
            if successSeat:
                success = True
                assigned_seat = i + 1 #他是座位123...我是格數012...
                break
        if not success:
            for i in range(0, len(current_sales), 2):
                successSeat = True
                for j in range(s_start, s_end):
                    if current_sales[i][j - 1] != 0:
                        successSeat = False
                        break
                if successSeat:
                    success = True
                    assigned_seat = i + 1 #他是座位123...我是格數012...
                    break

    # return the result
    return success, assigned_seat
# ===================================================


# ===================================================
# The input module

#讀初始資訊
first_line = input().split(',') 
seat_cnt = int(first_line[0])  # 座位
segment_cnt = int(first_line[1])  # 路段
passenger_cnt = int(first_line[2])  # 幾個人

passengers = [] #乘客資訊

# 讀每一個乘客資訊
for _ in range(passenger_cnt):
    passenger_data = input().split(',')
    s_start = int(passenger_data[0])  # Starting station
    s_end = int(passenger_data[1])    # Ending station
    c_pref = int(passenger_data[2])   # Seat preference (0: no preference, 1: odd, 2: even)
    passengers.append([s_start, s_end, c_pref])
# ===================================================


# ===================================================
# The computation module

current_sales = []
for _ in range(seat_cnt):
    one_seat = [0] * segment_cnt #先預設每個路段每個座位都沒人 : 0
    current_sales.append(one_seat)


# Process each passenger's request
for i in range(passenger_cnt):
    s_start, s_end, c_pref = passengers[i]
    # Try to assign a seat to the passenger
    success, assigned_seat = try_to_sell(current_sales, i + 1, c_pref, s_start, s_end)
    if success: #成功訂票 更新售票系統
        for station in range(s_start - 1, s_end - 1):
            current_sales[assigned_seat - 1][station] = i + 1  # Assign the passenger ID to the seat
# ===================================================


# ===================================================
# The output module

# Print the seat allocation map
for seat in current_sales:
    # Iterate through each segment in the seat
    for j in range(len(seat)):
        # Print the segment's status
        print(seat[j], end='')  # Print the number without newline
        # Print a comma if it's not the last segment
        if j < len(seat) - 1:
            print(',', end='')
    print()  # Print a newline after each seat
# ===================================================
