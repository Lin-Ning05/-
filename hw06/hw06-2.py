import datetime
num = int(input())
early = datetime.date(2026, 1, 1)
activities = []

for i in range(num):
    info = input().split(",")
    start = datetime.datetime.strptime(info[0], "%Y/%m/%d %H:%M")
    end = datetime.datetime.strptime(info[1], "%Y/%m/%d %H:%M")

    if start.date() != end.date() or start >= end:
        continue

    if early > start.date():
        early = start.date()
        activities = [(start, end)]
    elif start.date() == early:
        activities.append((start, end))

if len(activities) == 0:
    print(0)
else:
    activities.sort()
    over = 0
    for i in range(len(activities) - 1):
        for j in range(i + 1, len(activities)): 
            if activities[j][0] < activities[i][1]: # 比較j開始時間是否小於i結束時間
                over = 1
                break
        if over:
            break
    print(len(activities), end = ",")
    print(over)