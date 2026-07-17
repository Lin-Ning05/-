l_height = int(input()) * 100
result = ""
id = 1
while True:
    foot = int(input())
    if foot == -1:
        break
    inch = int(input())
    height = (12 * foot + inch) * 254
    if height > l_height:
        if result != "":
            result += ","
        result += str(id)
    id += 1
if result == "":
    print("-1")
else:
    print(result)