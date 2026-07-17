foot = int(input())
inch = int(input())

new_foot = foot + inch // 12
new_inch = inch % 12

print(str(new_foot) + ',' + str(new_inch))