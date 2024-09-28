'''
1. 최단거리이므로 우선 BFS
2. 이중리스트로 해결하려했으나 벽을 부숴야 하는 시점을 정확히 알 수 없다. 또한 하나씩 부수고 경로를 전부 돌려본다면
    NM^2 로 시간초과 발생
3. 따라서 벽을 부술지 말지 결정하기위해 삼중리스트를 사용한다.
'''
import sys
from collections import deque
# input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,s):
    q = deque()
    q.append((x,y,s))
    visited[x][y][s] = 1

    while q:
        cur = q.popleft()   # cur[0] = x, cur[1] = y, cur[2] = s
        if cur[0]==n-1 and cur[1]==m-1:
            return visited[cur[0]][cur[1]][cur[2]]
        for i in range(4):
            nx = dx[i] + cur[0]     # x축 위,아래,좌,우 순서
            ny = dy[i] + cur[1]     # y축
            if 0<=nx<n and 0<=ny<m:
                #벽을 부수지 않고 이동할때
                if graph[nx][ny]==0 and visited[nx][ny][cur[2]] == 0:
                    q.append((nx, ny, cur[2]))
                    visited[nx][ny][cur[2]] = visited[cur[0]][cur[1]][cur[2]]+1
                #벽을 부수고 이동할
                elif graph[nx][ny]==1 and cur[2] == 0:
                    q.append((nx, ny, cur[2] + 1))
                    visited[nx][ny][cur[2]+1] = visited[cur[0]][cur[1]][cur[2]]+1
    return -1

a = bfs(0,0,0)
print(a)

