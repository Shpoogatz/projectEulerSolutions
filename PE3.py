# this file contains a few solutions to the third project euler problem

# the first algorithm is buggy with squares and does not return the correct answer
# it is also the fatest least demanding

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

print n
