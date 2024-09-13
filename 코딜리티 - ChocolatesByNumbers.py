'''
Q.
Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.
You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).
You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.
The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:
def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates that you will eat.
For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:
N and M are integers within the range [1..1,000,000,000].

최대공약수 사용해서 쉽게 풀기
문제 자체가 원형 배열이라는 점에서 모듈로 연산을 생각 할 수 있고,
최대공약수를 사용하면 cnt를 쉽게 구할 수 있다.
'''
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def solution(N,M):
    z = gcd(N,M)
    return N//z

N=10
M=4
print(solution(N,M))