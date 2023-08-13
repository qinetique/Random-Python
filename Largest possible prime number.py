# Author: Tonmoy M
# https://qinetique.github.io
# Task - Largest possible prime number 

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def largest_permutation_prime(N):
    digits = sorted(str(N), reverse=True)
    largest_prime = -1

    def permutations(arr, l, r):
        nonlocal largest_prime
        if l == r:
            num = int(''.join(arr))
            if is_prime(num) and num > largest_prime:
                largest_prime = num
        else:
            for i in range(l, r + 1):
                arr[l], arr[i] = arr[i], arr[l]
                permutations(arr, l + 1, r)
                arr[l], arr[i] = arr[i], arr[l]  # backtrack

    permutations(digits, 0, len(digits) - 1)
    return largest_prime

N = int(input())
result = largest_permutation_prime(N)
print(result)
