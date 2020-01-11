"""
https://projecteuler.net/problem=4

Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def main():
    min_factor = 100
    max_factor = 999
    upper_limit = 999 * 999

    length = len(str(upper_limit))

    max_index = int(length/2) - 1

    # is_even_limit_length = length % 2 == 0

    preffix = int(str(upper_limit)[:max_index+1])
    original_preffix_lenght = len(str(preffix))

    result = None
    factor1 = None
    factor2 = None

    keep_trying = True
    while(keep_trying):
        if (len(str(preffix)) < original_preffix_lenght):
            raise ValueError('Not implemented')

        text = f'{str(preffix)}{str(preffix)[::-1]}'
        number = int(text)
        if number > upper_limit:
            preffix -= 1
            continue

        for component in range(999, 99, -1):
            if number % component != 0:
                continue

            quotient = int(number/component)
            if len(str(quotient)) == len(str(component)):
                keep_trying = False
                result = number
                factor1 = component
                factor2 = quotient
                break

        preffix -= 1       

    print(f'{result=};{factor1=};{factor2=}')

if __name__ == "__main__":
    main()