
"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def find_multiples(of, below):
    return set(of * count for count in range(1, int(below/of) + 1) if of * count < below)

def main():
    below = 1000
    of_list = [3,5]
    
    multiples_sets = [find_multiples(of= of_number, below= below) for of_number in of_list]
    union_set = set.union(*multiples_sets)
    multiples_sum = sum(union_set)

    print(f'Answer: {str(multiples_sum)}')

if __name__ == "__main__":
    main()