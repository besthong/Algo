'''
포도주를 마시지 않을 경우도 생각해야한다.
'''
case = int(input())
temp=[]
dp = [0]*case
for i in range(case):
    temp.append(int(input()))
if case == 1 or case == 2:
    print(sum(temp))
    quit()
dp[0]=temp[0]
dp[1]=temp[0]+temp[1]
dp[2]= max(temp[2]+temp[0], temp[2]+temp[1], dp[1])

result=0
for i in range(3,case):
    dp[i] = max(dp[i-3]+temp[i-1]+temp[i], dp[i-2]+temp[i],dp[i-1])
    # if i==len(temp)-1:
    #     result = max(dp[i-1],dp[i])

print(max(dp))