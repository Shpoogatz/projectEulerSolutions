# Euler 1
# this is my solution to Project Euler #1

toSum = []

# for i in the range 1 to 1000 check if the number is divisible by 3 or 5.
# if it is we append to toSum
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        toSum.append(i)

# to finish off the problem we output the sum of all the numbers in toSum
print(sum(toSum))
