from itertools import permutations
a,b = map(int,input().split())
temp=[i+1 for i in range(a)]
ans = list(permutations(temp,b))
for i in range(len(ans)):
    ans[i] = list(ans[i])
    for j in range(b):
        ans[i][j] = str(ans[i][j])
    print(" ".join(ans[i]))