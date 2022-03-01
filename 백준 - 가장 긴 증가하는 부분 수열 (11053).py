case = int(input())
temp = list(map(int,input().split()))
dp=[1]*case

for i in range(case):
    for j in range(i):
        if temp[i]>temp[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))