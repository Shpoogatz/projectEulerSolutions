# Project Euler 9
# my solution to Project Euler problem 9

# the first three lines are gathering our a b and c values
for a in range(1,1000):
    for b in range(1,1000):
        c = 1000 - a -b

        # if it is a pythagorean triplet we check if d is 1000
        if a**2 + b**2 == c**2:
            d = a + b + c

            # if d is 1000 we have found our goal, now print out the product of a b and c
            if d == 1000:
                print(a*b*c)
