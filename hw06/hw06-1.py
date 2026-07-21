info = input().split(",")
product_num = int(info[0])
size = int(info[1])
product = {}

for i in range(product_num):
    product_info = input().split(",")
    product_type = int(product_info[0])
    product_weight = int(product_info[1])
    product_range = product_weight // size

    if product_type not in product: 
        product[product_type] = []
    
    while len(product[product_type]) <= product_range: #補零直到對應區間
        product[product_type].append(0)
    product[product_type][product_range] += 1

target = int(input())
if target not in product:
    print("0")
else:
    for i in range(len(product[target])):
        if i < len(product[target]) - 1:
            print(product[target][i], end=',')
        else:
            print(product[target][i], end='')