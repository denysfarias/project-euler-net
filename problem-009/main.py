from time import perf_counter
import math

"""
https://projecteuler.net/problem=9

Special Pythagorean triplet

Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def naive_approach():
    max = 1000
    for a in range(1,max+1):
        for b in range(a+1, max+1):
            for c in range(b+1, max+1):
                if a**2 + b**2 == c**2 and a + b + c == 1000:
                    return a, b, c

    return None

def less_naive_approach():
    max = 1000
    for a in range(1, max+1):
        for b in range(a+1, max+1):
            c = 1000 - a - b
            if a ** 2 + b**2 == c**2:
                return a, b, c
    
    return None

# def trial_aproach():
#     max = 1000
#     squares = set()
    
#     for x in range(1,max+1):
#         if x == math.isqrt(x) ** 2:
#             squares.add(x)


def main():

    start = perf_counter()
    a, b, c = naive_approach()
    stop = perf_counter()
    time_in_sec = stop - start

    print(f'{a=},{b=},{c=} in {time_in_sec=}')

    start = perf_counter()
    a, b, c = less_naive_approach()
    stop = perf_counter()
    time_in_sec = stop - start

    print(f'{a=},{b=},{c=} in {time_in_sec=}')

if __name__ == "__main__":
    main()