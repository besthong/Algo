'''
3차원 리스트로 풀 수 있다.
맨처음 출력부분에서 graph=sum(graph,[]) 로 리스트를 합쳐서 한번에 max값과 0값을 찾으려 했는데
시간초과로 실패하여 그냥 3중 for문을 사용했다.
'''

from collections import deque
m,n,h = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
ans = 0

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]

for nh in range(h):
    for i in range(n):
        for j in range(m):
            if graph[nh][i][j]==1:
                q.append((nh,i,j))

def bfs():
    while q:
        cur = q.popleft()
        for i in range(6):
            nh = cur[0] + dh[i]
            nx = cur[1] + dx[i]
            ny = cur[2] + dy[i]

            if 0<=nx<n and 0<=ny<m and 0<=nh<h:
                if graph[nh][nx][ny] == 0:
                    q.append([nh,nx,ny])
                    graph[nh][nx][ny] = graph[cur[0]][cur[1]][cur[2]] + 1

bfs()
for h in graph:
    for i in h:
        for j in i:
            if j==0:
                print(-1)
                quit()
        ans = max(ans,max(i))
print(ans-1)