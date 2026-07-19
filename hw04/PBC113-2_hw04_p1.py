#===================================================
# The function

# k_num: integer
# return the difference between the largest and smallest number
def kaprekar_one_step(k_num):
    digit_list = []
    for i in range(4):
        n = k_num % 10
        digit_list.append(n)
        k_num //= 10
    min_num = sorted(digit_list)
    max_num = reversed(min_num)
    difference = int("".join(map(str, max_num))) - int("".join(map(str, min_num)))
    return difference
#===================================================

#===================================================
# The input module

# number: integer
# the variable "number" is the input number
number = int(input())
#===================================================

#===================================================
# The computation module

# getting the result of the Kaprekar routine
# initialize a list to store all numbers generated during the Kaprekar routine
all_numbers = []
new_number = number # initialize the new_number as the input number
# perform the Kaprekar routine until the number becomes 6174
while new_number != 6174:
    new_number = kaprekar_one_step(new_number)
    all_numbers.append(new_number) # append the result to the all_numbers list
if all_numbers == []:
    all_numbers.append(6174) # if the input number is already 6174, append 6174 to the all_numbers list
#===================================================



#===================================================
# The output module

# print the result as a comma-separated string
for i in range(len(all_numbers)):
    print(all_numbers[i], end = "")  # print the number
    if i < len(all_numbers) - 1:  # if it is not the last number, print a comma after the number
        print(",", end = "")
#===================================================
