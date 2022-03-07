# find the difference between the square of the sums of numbers from 1-100 and the sum of each number from 1-100 squared

sumof100 = 0
sumofsof100 = 0

for i in range(1,101):
    sumof100 += i

for i in range(1,101):
    i = i*i
    sumofsof100 += i

print((sumof100 * sumof100) - sumofsof100)
