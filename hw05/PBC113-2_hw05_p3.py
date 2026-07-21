def strGetInt(temp): #找數字
    for i in temp:
        if i.isdigit():
            return int(i)
        
def try_to_sell(current_sales, c_id, c_pref, s_start, s_end):
    # Initialize the return value: success and assigned_seat
    success = False
    assigned_seat = 0  # Set assigned_seat to 0 as default

    if c_pref == 0:
        for i in range(len(current_sales)):
            successSeat = True
            for j in range(s_start, s_end):
                if current_sales[i][j - 1] != "--":
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
                if current_sales[i][j - 1] != "--":
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
                    if current_sales[i][j - 1] != "--":
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
                if current_sales[i][j - 1] != "--":
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
                    if current_sales[i][j - 1] != "--":
                        successSeat = False
                        break
                if successSeat:
                    success = True
                    assigned_seat = i + 1 #他是座位123...我是格數012...
                    break

    return success, assigned_seat
# ===================================================


# ===================================================
# The input module

#讀初始資訊
first_line = input().split(',') 
seat_cnt = int(first_line[0])  # 座位
segment_cnt = int(first_line[1])  # 路段
passenger_cnt = int(first_line[2])  # 幾個人

current_sales = []
success_passengers = dict() #編號對應到首字母
for _ in range(seat_cnt):
    one_seat = ["--"] * segment_cnt #先預設每個路段每個座位都沒人 : 0
    current_sales.append(one_seat)

# Process each passenger's request
passengers = []
for i in range(passenger_cnt):
    line = input().strip()

    from_pos = line.find(" from ") #找 from 前面是名字，後面是資料
    name = line[:from_pos].strip()

    if "prefer window" in line:
        pref_pos = line.find("prefer window")
        c_pref = 1
    elif "no preference" in line:
        pref_pos = line.find("no preference")
        c_pref = 0
    elif "prefer aisle" in line:
        pref_pos = line.find("prefer aisle")
        c_pref = 2

    route = line[from_pos + 6 : pref_pos].strip()  # 跳過 " from "

    start_part, end_part = route.split("to") #用to分兩辦找數字
    s_start = strGetInt(start_part)
    s_end = strGetInt(end_part)

    passengers.append({
        "name": name,
        "s_start": s_start,
        "s_end": s_end,
        "c_pref": c_pref
    })

    # The computation module
    # Try to assign a seat to the passenger
    success, assigned_seat = try_to_sell(current_sales, i + 1, c_pref, s_start, s_end)
    if success:
        for station in range(s_start - 1, s_end - 1):
            current_sales[assigned_seat - 1][station] = i + 1
        success_passengers[i+1] = name[0].upper()
# ===================================================


# ===================================================
# The output module
char_counts = dict()
for p_id, first_char in success_passengers.items():
    char_counts[first_char] = char_counts.get(first_char, 0) + 1

id_map = dict() #編號對應結果
charNum = dict() #記錄第幾個出現

for p_id, first_char in success_passengers.items():
    if char_counts[first_char] == 1:
        id_map[p_id] = first_char * 2
    else:
        charNum[first_char] = charNum.get(first_char, 0) + 1
        id_map[p_id] = f"{first_char}{charNum[first_char]}"


for row in range(seat_cnt):
    for column in range(segment_cnt):
        target = current_sales[row][column]
        if target != "--":
            current_sales[row][column] = id_map[target] # 替換數字為縮寫
    print(",".join(current_sales[row]))
# ===================================================
