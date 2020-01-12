from time import perf_counter

"""
https://projecteuler.net/problem=7

10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def search_primes(position):
    if type(position) is not int or position < 1:
        raise ValueError('position must be positive int')
    
    begin_with = 2
    size = 120000
    step = 2

    sieve = []
    primes = []

    keep_searching = True
    while keep_searching:
        new_primes, new_sieve = search_primes_on_interval(begin_with= begin_with, up_to= size, primes_before= primes, stop_on_position= position)

        primes.extend(new_primes)

        if position <= len(primes):
            keep_searching = False
            continue

        sieve.extend(new_sieve)
        begin_with = size+1
        size *= step

    return primes

def search_primes_on_interval(begin_with, up_to, primes_before, stop_on_position= None):
    primes = []
    sieve = [[element, False] for element in range(begin_with, up_to+1)]

    for prime in primes_before:
        mark_sieve(sieve, prime)

    for index, pair in enumerate(sieve):
        is_marked = pair[1]
        if is_marked:
            continue

        number = pair[0]
        primes.append(number)
        if stop_on_position and len(primes_before) + len(primes) >= stop_on_position:
            break

        if number ** 2 > up_to:
            continue

        mark_sieve(sieve, number, index+1)
    
    return primes, sieve

def mark_sieve(sieve, prime, start_index= 0):
    for check_index in range(start_index, len(sieve)):
        check_pair = sieve[check_index]
        if check_pair[0] % prime == 0:
            check_pair[1] = True


def find_primes_1(up_to):
    primes = []
    sieve = [[element, False] for element in range(2, up_to+1)]
    for index, pair in enumerate(sieve):
        is_marked = pair[1]
        if is_marked:
            continue

        number = pair[0]
        primes.append(number)

        if number ** 2 > up_to:
            continue

        mark_sieve(sieve, number, index+1)

    return primes 

def find_primes_2(up_to):
    primes = []
    sieve = [[element, False] for element in range(2, up_to+1)]
    for index, pair in enumerate(sieve):
        is_marked = pair[1]
        if is_marked:
            continue

        number = pair[0]
        for check_index in range(index+1,len(sieve)):
            check_pair = sieve[check_index]
            if check_pair[0] % number == 0:
                check_pair[1] = True

        primes.append(number)

    return primes        

def find_primes_3(up_to):
    primes = []
    sieve = range(2, up_to+1)

    for number in sieve:
        if any(number % prime == 0 for prime in primes):
            continue

        primes.append(number)
    
    return primes

def comparing_primes():
    up_to = 10_000

    result = find_primes_1(up_to)

    start = perf_counter()
    result = find_primes_1(up_to)
    stop = perf_counter()
    
    print(f'{result=} in {stop-start} secs')

    start = perf_counter()
    result = find_primes_2(up_to)
    stop = perf_counter()

    print(f'{result=} in {stop-start} secs')

    start = perf_counter()
    result = find_primes_3(up_to)
    stop = perf_counter()

    print(f'{result=} in {stop-start} secs')

def main():
    position = 10_001

    start = perf_counter()
    primes = search_primes(position)
    result = primes[-1]
    stop = perf_counter()

    print(f'{result=} in {stop-start} secs')

if __name__ == "__main__":
    main()