
"""
https://projecteuler.net/problem=6

Sum square difference

Problem 6
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(up_to):
    return sum(element ** 2 for element in range(1, up_to+1))

def square_of_sum(up_to):
    return sum(range(1, up_to+1)) ** 2

def main():
    up_to = 100
    result = sum_of_squares(up_to) - square_of_sum(up_to)
    print(f'{result=}')

if __name__ == "__main__":
    main()