numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    for j in range(2, numbers[i]):
        if numbers[i] % j != 0:
            is_prime = False
            primes.append(numbers[i])
        elif numbers[i] % j == 0:
            is_prime = False
            not_primes.append(numbers[i])
            break



print(primes)
print(not_primes)



