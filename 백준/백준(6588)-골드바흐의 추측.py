import sys
import math


def sieve_of_eratosthenes(n):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False

    for start in range(2, int(n ** 0.5) + 1):
        if arr[start]:
            for multiple in range(start * start, n + 1, start):
                arr[multiple] = False

    primeNum = [num for num, is_prime in enumerate(arr) if is_prime]
    return primeNum


input = sys.stdin.read
data = list(map(int, input().strip().split()))
max_num = max(data)

primes = sieve_of_eratosthenes(max_num)
prime_set = set(primes)

for num in data:
    if num == 0:
        break
    found = False
    for prime in primes:
        if prime > num // 2:
            break
        if num - prime in prime_set:
            print(f"{num} = {prime} + {num - prime}")
            found = True
            break
    if not found:
        print("Goldbach's conjecture is wrong.")

# import sys
#
# def Sieve_of_Eratosthenes(n):
#     arr = [True for i in range(n+1)]
#     primeNum=[]
#     for i in range(2,int(n**0.5)+1):
#         if arr[i]==True: # 소수인경우
#             j=2
#             while i*j <= n:
#                 arr[i*j] = False
#                 j+=1
#
#     for i in range(2,n+1):
#         if arr[i]:
#             primeNum.append(i)
#     return primeNum
#
# input = sys.stdin.readline
# prime = set(Sieve_of_Eratosthenes(1000000))
#
# while True:
#     num = int(input().strip())
#     found = False
#     if num == 0: #0입력시 종료
#         break
#
#     else:
#         for i in prime:
#             if num - i in prime:
#                 print(f"{num} = {i} + {num-i}")
#                 found=True
#                 break
#     if found==False:
#         print("Goldbach's conjecture is wrong.")
#
#
#
#
#
#
