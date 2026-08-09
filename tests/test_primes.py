from src.naive import naive
from src.sqrt_bound import sqrt_bound
import pytest

ns = [0, 1, 2, 3, 4, 5, 10, 15, 30, 50, 100]

for n in ns:
    sqrt_method = sqrt_bound(n)
    naive_method = naive(n)
    methods = ['naive method', 'sqrt_bound']

    print(f'For n = {n} it ')
    if sqrt_method == naive_method:
        print('PASSED')

    else: print('FAILED')

    if n == len(sqrt_method) == len(naive_method):

        print(f'\nThe quantity n:{n} was reached.')
        
    else:

        x = len(sqrt_method) > len(naive_method)

        print(f'\nThe value of the {methods[x]} is inconsistent with the value of n: {n}')

    sqrt_is_prime = True
    naive_is_prime = True
    for prime_number in sqrt_method:

        for j in range(prime_number):

            if j == 0 or j == 1: continue

            if j**2 > prime_number: break

            if prime_number % j == 0:
                sqrt_is_prime = False
                break

    if not sqrt_is_prime:
        print(f'\nThe sqrt_bound is wrong.')
    else: print(f'\nThe sqrt_bound is correct')

    for prime_number in naive_method:

        for j in range(prime_number):

            if j == 0 or j == 1: continue

            if j**2 > prime_number: break

            if prime_number % j == 0:
                naive_is_prime = False
                break

    if not naive_is_prime:
        print(f'\nThe naive method is wrong.')
    else: print(f'\nThe naive method is correct')
    sqrt_is_in_ascending_order = True
    naive_is_in_ascending_order = True
    for i in range(n-1):
        if(sqrt_method[i] >= sqrt_method[i+1]): sqrt_is_in_ascending_order = False
        if(naive_method[i] >= naive_method[i+1]): naive_is_in_ascending_order = False

    if not sqrt_is_in_ascending_order:
        print("\nThe sqrt_bound is not in ascending order")
    else:
        print("\nThe sqrt_bound is in ascending order")

    if not naive_is_in_ascending_order:
        print("\nThe naive method is not in ascending order")
    else:
        print("\nThe naive method is in ascending order")

    sqrt_bound_uniqueness = True
    naive_uniqueness = True

    for num in sqrt_method:
        k = 0
        for prime in sqrt_method:
            if(num == prime):
                k+=1

        if k!=1:
            sqrt_bound_uniqueness = False

    if not sqrt_bound_uniqueness:
        print(f'\nThe sqrt_bound is not unique')
    else:
        print(f'\nThe sqrt_bound is unique')

    for num in naive_method:
        k = 0
        for prime in naive_method:
            if(num == prime):
                k+=1

        if k!=1:
            naive_uniqueness = False

    if not naive_uniqueness:
        print(f'\nThe naive method is not unique')
    else:
        print(f'\nThe naive method is unique')

    if n>=1:
        if sqrt_method[0] == 2:
            print('\nsqrt_bound did not skip an element.')
        else:
            print('\nsqrt_bound skipped element.')

        if naive_method[0] == 2:
            print('\nnaive method did not skip an element.')
        else:
            print('\nnaive method skipped element.')

    else:
        print('\nn == 0.')