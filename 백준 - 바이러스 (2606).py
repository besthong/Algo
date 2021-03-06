'''
한번 타고 들어갈 때 끝까지 가서 연결이 되어있나 확인이 필요하니
DFS를 사용했다.
'''

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

    return visited

visited=[False]*(n+1)
dfs(graph,1,visited)
print(visited.count(True)-1)