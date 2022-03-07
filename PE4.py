# Find the largest palindrome that is a mulitple of two three digit numbers

# for j 101-999 and i range 101-999 we multiple them together and set it to sum,
# the sum is then set to a string and checked if it is the same forwards as it is backwards
# if it is check if its larger than our current largest palindrome
# if it is, the sum becomes out current largest palindrome


currentLargestPal = 0

for i in range(101,999):
    for j in range(101,999):
        sum = i*j
        sum = str(sum)
        if sum == sum[::-1]:
            sum = int(sum)
            if sum > currentLargestPal:
                currentLargestPal = sum


print(currentLargestPal)
