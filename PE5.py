# multiple solutions to PE 5

# this worlds but takes forever becasue the loop can get up to 19 before realizing it does not work
'''num = 2520
i = 2
while i < 21:
    if num % i == 0:
        i += 1
    else:
        num += 1
        i = 2
print(num)'''

# the better solution...
check_list = [11, 13, 14, 16, 17, 18, 19, 20]

# we input the step as the highest number that we want to check for
def find_solution(max(check_list)):
    for num in range(step, 999999999, step): # did 99999999 beacause just assuming the val is less than that
        if all(num % n == 0 for n in check_list): # if all numbers in the checklist divide into the current num
            return num # return the num
    return None

solution = find_solution(20)
