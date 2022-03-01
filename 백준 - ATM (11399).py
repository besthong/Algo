case = int(input())
temp = sorted(list(map(int,input().split())))
ans=0
for i in range(len(temp)):
    ans+=sum(temp[:i+1])
print(ans)