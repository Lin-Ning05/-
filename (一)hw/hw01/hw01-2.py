first_foot = int(input())
first_inch = int(input())

second_foot = int(input())
second_inch = int(input())

third_foot = int(input())
third_inch = int(input())

height = int(input())
count = 0


if (12 * first_foot + first_inch) * 2.5 > height:
    count += 1
if (12 * second_foot + second_inch) * 2.5 > height:
    count += 1
if (12 * third_foot + third_inch) * 2.5 > height:
    count += 1

print(count)
