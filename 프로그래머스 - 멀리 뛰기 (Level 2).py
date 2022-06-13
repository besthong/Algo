'''
두가지로 풀어봤다.
1. dp
2. itertools 의 product

1번은 쉽게 풀 수 있었고,
2번은 복습한번 해보고자 product로 사용하여 풀어봤다.
중복값이 필요하여 product를 사용하였고, 각 한자리수, 두자리수 ~ n의자리수 까지
list화 하여 sum이 n과 같을경우 answer+=1을 하여 return 하도록 했으며
당연히 시간초과,메모리초과를 예상했다.

제출은 1번으로
'''
#dp 풀이
def solution(n):
    answer = 0

    if n == 1 or n == 2:
        return n
    else:
        dp = [0]*n
        dp[0]=1; dp[1]=2

        for i in range(2,n):
            dp[i]=(dp[i-1]+dp[i-2])%1234567

        answer = dp[i]
        return answer

#product 풀
from itertools import combinations
from itertools import product

def solution(n):
    answer=0
    onetwo = [1,2]
    for i in range(1,n+1):
        for j in product(onetwo,repeat=i):
            j = list(j)
            if sum(j) == n:
                answer+=1
    return answer
n = 4
print(solution(n))