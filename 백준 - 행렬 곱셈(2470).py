n,m = map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
m,k = map(int,input().split())
b=[list(map(int,input().split())) for _ in range(m)]

ans=[[0]*k for _ in range(n)]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            ans[i][j] += a[i][k] * b[k][j]

for i in ans:
    for j in i:
        print(j,end=' ')
    print()