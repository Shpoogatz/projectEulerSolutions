# Euler 2
# this is my solution to Project-Euler #2

limit = 4000000
x,y = 1,2 # the problem says our first two fib numbers are 1 and 2
limiter = 0 # we will say while this is less than our limit
countEvens = 0 # the problem requires the sum of the even fibs

# while our limiter is less than the limit we increase the limiter by x
# z is equal to x + y (z is solely to save the value of x+y)
# x becomes y and y becomes z
# both of our numbers have increased and are the next fibonacci number
while limiter <= limit:
    limiter += x
    z = x + y
    x = y
    y = z
    # if x is even add it to the countEvens variable
    if x % 2 == 0:
        countEvens += x

# print out our countEvens variable for the answer
print(countEvens)
