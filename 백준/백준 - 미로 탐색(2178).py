from collections import deque
n,m = map(int,(input().split()))
graph = [list(map(int,input())) for _ in range(n)]

visited=[[False]*m for _ in range(n)]
distance= [[1]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        cur = q.popleft()
        for i in range(4):
            nx = cur[0]+dx[i]
            ny = cur[1]+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if graph[nx][ny]==1 and visited[nx][ny]==False:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    distance[nx][ny] = distance[cur[0]][cur[1]]+1

    return distance

ans = bfs(0,0)
print(ans[-1][-1])
