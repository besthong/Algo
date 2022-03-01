case = int(input())
temp = [list(map(int,input().split())) for _ in range(case)]
temp=temp[::-1]

for i in range(len(temp)-1):
    for j in range(len(temp[i+1])):
        temp[i+1][j] += max(temp[i][j],temp[i][j+1])

ans=temp[-1]
print(ans[0])