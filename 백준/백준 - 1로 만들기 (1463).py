num = int(input())

dp = [999999 for i in range(max(4,num+1))]
dp[0]=0; dp[1]=0; dp[2]=1; dp[3]=1
for i in range(4,num+1):
    dp[i] = min(dp[i-1]+1,dp[i])
    if i%2==0:
       dp[i]=min(dp[i//2]+1,dp[i])
    if i % 3 == 0:
       dp[i] = min(dp[i//3] + 1, dp[i])

print(dp[num])