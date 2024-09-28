'''
3
4 10 20 30 40
3 7 5 12
3 125 15 25
'''

import sys
from itertools import combinations

input=sys.stdin.readline

case = int(input())
def gcd(a,b):
    while b:
        a,b = b, a % b
    return a

for i in range(case):
    numbers = list(map(int,input().strip().split()))
    numbers = numbers[1:]

    ans=0

    for a,b in combinations(numbers,2):
        ans += gcd(a,b)

    print(ans)
