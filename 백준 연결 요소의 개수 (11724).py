'''
틀린이유
1. 최대 재귀 호출 지정안해줬더니 recursion limit error
2. pypy로 제출했더니 memory exception
3. python으로 제출했더니 timeout -> input을 readline으로 변경
4. 마지막 반복문에서 n+1을 안하고 n으로 해서 출력 1개 부족해서 에러
하하..
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

def dfs(graph, v, visited):
    if visited[v] == 1: return
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    return visited

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0 for _ in range(n+1)]
ans=0
for i in range(n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        ans+=1
print(ans-1)
