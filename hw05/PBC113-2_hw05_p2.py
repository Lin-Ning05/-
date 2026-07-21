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

passengers = []
passenger_names = [] #乘客全名

for _ in range(passenger_cnt):
    line = input().strip()
    
    name, detail = line.split(':')
    passenger_names.append(name)
    route_part, pref_part = detail.split(',')
    
    route_tokens = route_part.split()
    s_start = int(route_tokens[1][0])
    s_end = int(route_tokens[3][0])

    pref_str = pref_part.strip()

    if pref_str == "no preference":
        c_pref = 0
    elif pref_str == "prefer window":
        c_pref = 1
    elif pref_str == "prefer aisle":
        c_pref = 2
        
    passengers.append([s_start, s_end, c_pref])
# ===================================================


# ===================================================
# The computation module

current_sales = []
for _ in range(seat_cnt):
    one_seat = [0] * segment_cnt #先預設每個路段每個座位都沒人 : 0
    current_sales.append(one_seat)


# Process each passenger's request
failed_passengers = []
for i in range(passenger_cnt):
    s_start, s_end, c_pref = passengers[i]
    # Try to assign a seat to the passenger
    success, assigned_seat = try_to_sell(current_sales, i + 1, c_pref, s_start, s_end)
    if success: 
        for station in range(s_start - 1, s_end - 1):
            current_sales[assigned_seat - 1][station] = i + 1  
    else:
        # 訂票失敗，記錄名字
        failed_passengers.append(passenger_names[i])
# ===================================================


# ===================================================
# The output module
if len(failed_passengers) == 0:
    print("0")
else:
    print(",".join(failed_passengers))
# ===================================================
