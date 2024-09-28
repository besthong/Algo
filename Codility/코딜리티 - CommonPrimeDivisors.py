'''
소인수분해 했을때, 소수로 이루어진 배열이 같은지 확인하는 문제
ex) A=15, B=75 일 떄, 둘의 g=GCD는 15이다.
이 때 각 숫자를 g로 나누고, 결과가 1만 남으면 둘의 소인수분해 리스트는 일치한다.
'''
import math

def gcd(a, b):
    return math.gcd(a, b)

# N에서 공통 소인수들로만 나누어지는지 확인하는 함수
def remove_prime_factors(n, gcd_val):
    gcd_factor = gcd(n, gcd_val)

    # n이 gcd_val의 소인수들로 나누어 떨어질 때까지 나눔
    while gcd_factor != 1:
        n //= gcd_factor
        gcd_factor = gcd(n, gcd_val)

    return n

def has_same_prime_divisors(N, M):
    G = gcd(N, M)

    # N과 M을 최대공약수로 나눈 후 남은 값이 모두 1인지 확인
    N = remove_prime_factors(N, G)
    M = remove_prime_factors(M, G)

    return N == 1 and M == 1


def solution(A, B):
    count = 0
    for N, M in zip(A, B):
        if has_same_prime_divisors(N, M):
            count += 1
    return count


A=[15,10,3]
B=[75,30,5]
print(solution(A,B))