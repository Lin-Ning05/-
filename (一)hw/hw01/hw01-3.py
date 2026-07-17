foot = int(input())
inch = int(input())
height_integer = int(input())
height_decimal = int(input())

if (12 * foot + inch) * 254 > height_integer * 100 + height_decimal:
    print("Yes")
else:
    print("No")