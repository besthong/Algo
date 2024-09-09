def solution(n):
    answer = 0

    if n==1 or n==2:
        return 1

    dp = [0]*(n)
    dp[0]=1
    dp[1]=2
    for i in range(2,n):
        dp[i]=dp[i-1]+dp[i-2]
        dp[i]%=10000007
    return sum(dp)

# 1 2 3 5
# 4-> 11
# 6-> 41
# 8-> 153


n = 6
print(solution(n))