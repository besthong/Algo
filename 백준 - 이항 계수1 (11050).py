# 파스칼법칙 & dp
# n,k = n-1,k-1 + n-1,k

a,b = map(int,input().split())

# dp = [[0]*(a+1) for _ in range(b+1)]
dp = [[0 for _ in range(a+1)] for _ in range(a+1)]

for i in range(a+1):
    dp[i][i] = 1
    dp[i][0] = 1

for i in range(2,a+1):
    for j in range(1, a+1):
        if dp[i][j] != 1:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
print(dp[a][b])



