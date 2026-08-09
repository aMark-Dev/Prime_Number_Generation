def sqrt_bound(n):
    prime_numbers_list = [2]

    k = prime_numbers_list[0] + 1

    while n > len(prime_numbers_list):

        for num in prime_numbers_list:

            if k % num == 0: break

            if num**2 > k:
                prime_numbers_list.append(k)
                break

        k+=1

    #If you want the list of prime numbers, you do use:
    return prime_numbers_list