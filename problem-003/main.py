import math

"""
https://projecteuler.net/problem=3

Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
def find_primes_up_to(number):
    sieve = set(range(2, number+1))
    for factor in range(2,int(math.sqrt(number))+1):
        if factor not in sieve:
            continue

        sieve = set(element for element in sieve if element == factor or element % factor != 0)
    
    return sieve

def find_prime_factors(target):
    primes = sorted(find_primes_up_to(target))
    
    index = 0
    quotient = target
    factors = set()
    while (quotient != 1):
        factor = primes[index]
        if quotient % factor == 0:
            quotient = int(quotient/factor)
            factors.add(factor)
        else:
            index += 1

    return factors

def find_prime_factors_2(target):
    primes = set()
    prime_factors = set()
    quotient = target
    for number in range(2, target+1):
        if any(number % prime == 0 for prime in primes):
            continue

        primes.add(number)
        
        keep_trying = True
        while(keep_trying):
            if quotient % number == 0:
                quotient = int(quotient/number)
                prime_factors.add(number)
            else:
                keep_trying = False
        
        if quotient == 1:
            break
    
    return prime_factors

def main():
    target = 600851475143

    prime_factors = find_prime_factors_2(target)

    max_prime_factor = max(prime_factors)

    print(f'Answer: {str(max_prime_factor)}')

if __name__ == "__main__":
    main()