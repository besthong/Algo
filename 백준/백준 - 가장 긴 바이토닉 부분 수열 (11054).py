# 10
# 1 5 2 1 4 3 4 5 2 1
# 10 20 30 25 20
'''
reverse로 동시에 조회한다.
'''
case = int(input())
temp = list(map(int,input().split()))
temp_reverse = temp[::-1]
dp1 = [1]*case
dp2 = [1]*case
for i in range(case):
    for j in range(i):
        if temp[i]>temp[j]:
            dp1[i] = max(dp1[i],dp1[j]+1)
        if temp_reverse[i]>temp_reverse[j]:
            dp2[i] = max(dp2[i],dp2[j]+1)

result = [0]*case
for i in range(case):
    result[i] = dp1[i]+dp2[case-1-i]-1

print(max(result))