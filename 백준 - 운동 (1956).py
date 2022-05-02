'''
플로이드 와샬로 풀 수 있다.
포인트는 모든 정점의 최단거리를 구하고 (플로이드와샬)
graph[i][i] 가 inf 가 아닌경우, 사이클이 있다고 간주한다.
이유는 i->i 가 inf보다 작다고할경우 어떤 정점을 거쳐 다시 돌아왔을경우(사이클)이
존재하기때문.
'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[float('inf')]*n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

answer=float('inf')
for i in range(len(graph)):
    answer=min(answer,graph[i][i])

if answer==float('inf'):
    print(-1)
else:
    print(answer)

