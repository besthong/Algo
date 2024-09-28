'''
평범한 냅색 문제
문제중 무게 등이 쪼개질 수 없는경우 DP를 사용하여 풀 수 있고,
무게 등을 쪼갤 수 있는 경우 Greedy 로 접근 할 수 있다.
'''
n,k = map(int,input().split())
bag=[[0,0]]
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(n):
    bag.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        if bag[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j] , dp[i-1][j-bag[i][0]]+bag[i][1])
print(dp[n][k])