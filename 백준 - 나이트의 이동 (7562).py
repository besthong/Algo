'''
나이트가 갈 수 있는 방향 8개
따라서 8개 방향으로 각각 BFS 진행하면 쉽게 풀 수 있다.
원하는 좌표값 도착시 바로 return 해야 불필요한 이후 작업을 안한다.
'''
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1, 1,2,2,1,-1,-2]

def bfs(x,y,end_x,end_y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 1

    while q:
        cur = q.popleft()
        if cur[0]==end_x and cur[1]==end_y:
            return graph[cur[0]][cur[1]]-1
        for i in range(8):
            nx = cur[0]+dx[i]
            ny = cur[1]+dy[i]

            if 0<=nx<sz and 0<=ny<sz and graph[nx][ny]==0:
                q.append((nx,ny))
                graph[nx][ny] = graph[cur[0]][cur[1]]+1

case = int(input())
for _ in range(case):
    sz = int(input())
    graph = [[0]*sz for _ in range(sz)]
    start_x,start_y = map(int,input().split())
    end_x,end_y = map(int,input().split())

    if start_x == end_x and start_y == end_y:
        print(0)
        continue
    ans = bfs(start_x,start_y,end_x,end_y)
    print(ans)
