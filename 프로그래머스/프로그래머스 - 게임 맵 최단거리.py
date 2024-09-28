'''
전형적인 BFS 문제
행렬이 주어졌을 때 최단거리 구하기
네 방향으로 접근 할 수 있어야 하므로 dx,dy 사용
visited 변수로 이미 방문한곳은 방문하지않도록 처리
'''
from collections import deque

def solution(maps):
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]

    def bfs(x,y):
        q = deque()
        q.append((x,y))

        visited[x][y] = True

        dx=[-1,1,0,0]
        dy=[0,0,-1,1]

        while q:
            cur = q.popleft()

            for i in range(4):
                nx = cur[0] + dx[i]
                ny = cur[1] + dy[i]

                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if maps[nx][ny]==1 and visited[nx][ny]==False:
                        visited[nx][ny]==True
                        q.append((nx, ny))
                        maps[nx][ny] = maps[cur[0]][cur[1]]+1

        return maps[-1][-1]
    answer = bfs(0,0)
    if answer == 1:
        answer = -1
    return answer

maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))