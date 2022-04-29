'''
0-1 BFS 알고리즘 사용
핵심은 가중치가 0인 간선을 우선순위로 처리하기위해 Deuqe.appendleft() 로 먼저 처리하도록 유도
'''

from collections import deque

n,k = map(int,input().split())
q = deque()
q.append(n)
visited = [-1 for _ in range(100001)]   # 최대 정점 개수 100,000 보다 +1
visited[n] = 0

while q:
    cur = q.popleft()
    if cur == k:
        print(visited[cur])
        break
    if 0<cur*2<100001 and visited[cur*2] == -1:
        visited[cur*2] = visited[cur]
        q.appendleft(cur*2)
    if 0<=cur-1<100001 and visited[cur-1] == -1:
        visited[cur-1] = visited[cur]+1
        q.append(cur-1)
    if 0<=cur+1<100001 and visited[cur+1] == -1:
        visited[cur+1] = visited[cur]+1
        q.append(cur+1)


