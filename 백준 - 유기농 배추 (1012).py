'''
DFS를 사용하여 쉽게 풀 수 있다.
해당 문제에서는 파이썬 기본으로 걸려있는 재귀함수 최대횟수(1000회) 가 넘어가서 에러가 발생한다.
따라서 sys.setrecursionlimit(10**5)까지 재귀 할 수 있도록 설정한다.
'''
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