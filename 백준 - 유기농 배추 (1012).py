import sys
sys.setrecursionlimit(10**5)

case = int(input())

dx=[-1,1,0,0]
dy=[0,0,1,-1]

ans=[]
def dfs(x,y):
    global count
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]==1:
        # count+=1
        graph[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)
        return True

for _ in range(case):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for i in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1
    count=0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                count+=1
    print(count)