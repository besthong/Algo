from itertools import permutations
a,b = map(int,input().split())
temp=[i+1 for i in range(a)]
ans = list(permutations(temp,b))
for i in range(len(ans)):
    ans[i] = list(ans[i])
    for j in range(b):
        ans[i][j] = str(ans[i][j])
    ans[i].sort()

realans = []

for i in ans:
    if i not in realans:
        realans.append(i)

for i in realans:
    print(" ".join(i))