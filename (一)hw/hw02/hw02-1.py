first_foot = int(input())
first_inch = int(input())

second_foot = int(input())
second_inch = int(input())

third_foot = int(input())
third_inch = int(input())

first_height = 12 * first_foot + first_inch
second_height = 12 * second_foot + second_inch
third_height = 12 * third_foot + third_inch

max = first_height
id = 1

if second_height > max:
    max = second_height
    id = 2
if third_height > max:
    max = third_height
    id = 3

print(str(max //12) + "," + str(max % 12) + "," + str(id))
