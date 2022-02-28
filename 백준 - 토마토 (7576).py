# from collections import deque
#
# m,n = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]
#
# dx = [-1,1,0,0]
# dy = [0,0,1,-1]
#
# def bfs(x,y):
#     q = deque()
#     q.append((x,y))
#
#     while q:
#         cur = q.popleft()
#         for i in range(4):
#             nx = cur[0] + dx[i]
#             ny = cur[1] + dy[i]
#
#             if 0<=nx<n and 0<=ny<m:
#                 if graph[nx][ny] == 0:
#
#                     graph[nx][ny]=graph[cur[0]][cur[1]]+1
#                     q.append((nx, ny))
#     return graph
#
# ans=[]
# for i in range(n):
#     for j in range(m):
#         if graph[i][j]==1:
#             ans=bfs(i,j)
#             # print(ans1,ans2)
#
# print(*ans, sep='\n')
#
#

# 위에는 내 틀린 코드.. 문제점은 토마토가 두개 이상이 익어있을때(1일때) q에 미리 넣지 않고, bfs를 실행했을때
# 안에서 큐를 돌렸다. 그래서 문제는 1번 토마토에서 전부 합산하고, 2번토마토가 할게 없어져 값이 틀렸다.

from collections import deque
m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

def bfs():
    while q:
        cur = q.popleft()
        for i in range(4):
            nx = dx[i]+cur[0]
            ny = dy[i]+cur[1]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[cur[0]][cur[1]]+1
                    q.append((nx,ny))

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            quit()
    ans = max(ans,max(i))
print(ans-1)



