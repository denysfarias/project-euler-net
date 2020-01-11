from collections import defaultdict, Counter

"""
https://projecteuler.net/problem=5

Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def find_smallest_positive_number_evenly_divisible(max_number):
    divisibles = range(2, max_number+1)
    number = max_number

    while(True):
        if all(number % element == 0 for element in divisibles):
            return number
        
        number += 1

def find_smallest_positive_number_evenly_divisible_2(max_number):
    divisibles = range(2, max_number+1)
    outer_factors = defaultdict(int)

    for outer_index, divisible in enumerate(divisibles):
        quotient = divisible
        inner_factors = defaultdict(int)
        for inner_index in range(0,outer_index+1):

            inner_factor = divisibles[inner_index]
            while True:
                if quotient % inner_factor == 0:
                    quotient = int(quotient/inner_factor)
                    inner_factors[inner_factor] += 1
                else:
                    break

            if quotient == 1:
                max_items = Counter(inner_factors) | Counter(outer_factors)
                outer_factors = defaultdict(int, max_items)
                break
    
    total = 1
    for key in outer_factors:
        total *= key ** outer_factors[key]
    
    return total

def main():
    result = find_smallest_positive_number_evenly_divisible_2(20)

    print(f'{result=}')

if __name__ == "__main__":
    main()