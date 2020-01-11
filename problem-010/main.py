from time import perf_counter

"""
https://projecteuler.net/problem=10

Summation of primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def naive_approach():
    pass

def main():

    start = perf_counter()
    primes, primes_sum = naive_approach()
    stop = perf_counter()
    time_in_sec = stop - start

    print(f'{primes=}, {primes_sum} in {time_in_sec=}')

if __name__ == "__main__":
    main()