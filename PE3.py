# https://levelup.gitconnected.com/solve-and-understand-the-project-euler-problems-in-python-introduction-and-problems-1-3-32625d1633f7

# the first algorithm is buggy with squares and does not return the correct answer
# it is also the fatest least demanding

number = 600851475143

for prime_factor in range(2, int(math.sqrt(number)) + 1):
    while number % prime_factor == 0:
        number = number / prime_factor
        if number == 1 or number == prime_factor:
            print(prime_factor)
            break
