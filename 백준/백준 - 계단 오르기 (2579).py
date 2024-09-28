case = int(input())
temp=[]
dp=[0]*case
for i in range(case):
    temp.append(int(input()))
if case==1:
    print(temp[-1])
    quit()
elif case == 2:
    print(temp[0]+temp[1])
    quit()
dp[0] = temp[0]
dp[1] = max(temp[0]+temp[1], temp[1])
dp[2] = max(temp[1]+temp[2], temp[0]+temp[2])
for i in range(3,len(temp)):
    dp[i] = max(dp[i-2]+temp[i], dp[i-3]+temp[i-1]+temp[i])
print(dp[-1])