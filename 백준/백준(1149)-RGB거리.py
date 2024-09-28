'''
3
26 40 83
49 60 57
13 89 99


li=[[26,40,83],[49,60,57],[13,89,99]]
dp=[[26,40,83],[49,60,57],[13,89,99]]
'''
n=int(input())

li=[]
for i in range(n):
    temp=list(map(int,input().split()))
    li.append(temp)

dp=li.copy()

for i in range(1,n):
    for j in range(3):
        if j==0:
            dp[i][j]=min(dp[i-1][j+1]+li[i][j], dp[i-1][j+2]+li[i][j])
        elif j==1:
            dp[i][j]=min(dp[i-1][j-1]+li[i][j], dp[i-1][j+1]+li[i][j])
        elif j==2:
            dp[i][j]=min(dp[i-1][j-2]+li[i][j], dp[i-1][j-1]+li[i][j])

print(min(dp[-1]))
