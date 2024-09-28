'''
각 가로길이 당 타일이 몇개 씩 들어가는지 세어보니
피보나치 규칙을 발견했고
그에맞춰서 dp로 해결 가능했으나
return 값에서 나머지연산 처리를 해줬더니 시간초과가 발생하여
+연산시 나머지연산 처리를 하여 통과
'''
def solution(n):
    answer = 0
    if n == 1 or n == 2:
        return n
    else:
        dp = [0] * n
        dp[0] = 1;
        dp[1] = 2
        for i in range(2,n):
            dp[i]=(dp[i-1]+dp[i-2])%1000000007
        answer = dp[n-1]

        return answer


#n = 1 -> 1
#n = 2 -> 2
#n = 3 -> 3
#n = 4 -> 5

n = 7
print(solution(n))