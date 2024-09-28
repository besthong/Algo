case = int(input())
def bc(a,b):
    dp=[[0]*(a+1) for _ in range(a+1)]

    for i in range(a+1):
        dp[i][i] = 1
        dp[i][0] = 1
    for i in range(2,a+1):
        for j in range(1,a+1):
            if dp[i][j] != 1:
                dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
    return dp[a][b]
for i in range(case):
    a,b = map(int,input().split())
    if a<b:
        a,b=b,a
    print(bc(a,b))

