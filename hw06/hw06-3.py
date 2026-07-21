k, num, weight1, weight2, weight3 = map(int, input().split(","))
customer = []

for i in range(num):
    info = input().split(",")
    age, income, membership = map(int, info[:3])
    debt = info[3]
    if age * 12 - membership < 18 * 12:
        continue
    customer.append([age, income, membership, debt, i + 1])

new_age, new_income, new_membership = map(int, input().split(','))
distances = []

for i in range(len(customer)):
    d = (weight1 * (customer[i][0] - new_age) ** 2 + 
         weight2 * (customer[i][1] - new_income) ** 2 + 
         weight3 * (customer[i][2] - new_membership) ** 2)

    distances.append((d, customer[i][4], customer[i][3])) # 距離, 編號, 是否欠卡債

if len(distances) < k:   # 有效客戶數小於k
    print(0)
else:
    distances.sort()
    yes_count = 0
    no_count = 0
    for i in range(k):
        if distances[i][2] == "Y":
            yes_count += 1
        else:
            no_count += 1

    print(distances[0][1], end=',')
    if yes_count > no_count:
        print("Y")
    else:
        print("N")
