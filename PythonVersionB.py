from math import sqrt
from time import time

def is_a_square(n: int) -> bool:
        return round(sqrt(n))**2 == n

# Checks an integer to see if it is prime or not by
def is_prime(n: int) -> bool:
    if n % 2 == 0 and n > 2:
        return False
    # range starts at 3, increments by 2, and ends at 1 greater than the int
    # value of the square root of the checked number (range is not inclusive
    # for the ending value). Anything with a remainder of 0 will return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))

# takes argument for number of fails to include in output list
def goldbach_fails(bound: int) -> [int]:
    primes: [int] = [2]
    oddNumber: int = 3
    fails: [int] = []

    while len(fails) < bound:
        if is_prime(oddNumber):
            primes.append(oddNumber)
        else:
            for prime in primes:
                if is_a_square(((oddNumber-prime)//2)):
                    break
            # optional else that executes if above for loop completes without a break
            else:
                fails.append(oddNumber)
        oddNumber += 2
    return fails

results = 0
print(goldbach_fails(2))

for _ in range(100):
    start = time()
    goldbach_fails(2)
    end = time()
    results += end - start

print("Average time: ", results/100)
