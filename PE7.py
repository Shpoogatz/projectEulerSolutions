#$Brute Force Method 10001st Prime
#https://www.youtube.com/watch?v=gLlTlpe9KkI

numberToFind = 10001
x = 2
listOfPrimes = []

while(len(listOfPrimes) < numberToFind):
    if all(x % prime for prime in listOfPrimes): #1
        listOfPrimes.append(x)
    x += 1
print(listOfPrimes[-1])

#1
#same as
'''
for prime in listOfPrimes:
    if x % prime:
        pass#do something
'''
# This would only need one of the 'prime' variables to fit the if statement.
# Calling a single line for if loop with all() requires all primes in the for if to satisfy the for if.

