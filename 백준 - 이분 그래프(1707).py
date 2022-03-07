'''
주의점
1. 그래프는 항상 연결된게 아님
2. 답은 대문자...
3. 최대 재귀횟수를 지정해주자. 여기선 10^6 으로 진행함


Note. visited = []*n 으로 했다가 에러가 났다 생각해보니 약한참조, 강한참조 차이 때문에
      visited = [[] for _ in range(n)] 으로 바꿔서 진행했다.
'''
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph,v,visited,color):
    global ans
    visited[v][0] = 1
    visited[v][1] = color

    for i in graph[v]:
        if not visited[i][0]:
            dfs(graph,i,visited,-color)
        elif visited[i][1] == -color:
            pass
        else:
            ans = "NO"
            return

case = int(input())
for _ in range(case):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]

    visited = [[0,0] for _ in range(v+1)]
    ans = "YES"
    for i in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(v):
        if visited[i][0]==0:
            dfs(graph,i,visited,1)
    print(ans)