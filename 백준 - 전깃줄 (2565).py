case = int(input())
temparr = []
a = [0] * case
b = [0] * case
for i in range(case):
    temp = list(map(int, input().split()))
    temparr.append(temp)

temparr = sorted(temparr, key=lambda x: x[0], reverse=False)

for i in range(len(temparr)):
    a[i] = temparr[i][0]
    b[i] = temparr[i][1]

dp = [1] * case

for i in range(case):
    for j in range(i):
        if b[i] > b[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(len(b) - max(dp))


