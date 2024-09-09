'''
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

1
3 2
1 3
2 3

1
4 4
1 2
2 3
3 4
4 2

'''

from collections import deque
import sys
input=sys.stdin.readline
case = int(input())

def bfs(graph,start,visited):
    dq=deque([start])
    visited[start]= 1
    cur_num=1
    while dq:
        cur = dq.popleft()
        for i in graph[cur]:
            if not visited[i]:
                visited[i]=-visited[cur]
                dq.append(i)
            elif visited[i] == visited[cur]:
                return False
    return True

for _ in range(case):
    v,e = map(int,input().split()) # 3,2
    graph=[[] for _ in range(v+1)]
    visited=[0]*(v+1)

    for i in range(e):
        a, b = map(int, input().split())  # 1,3 / 2,3
        graph[a].append(b)
        graph[b].append(a)

    t = True
    for i in range(1,v+1):
        if visited[i] == 0:
            if not bfs(graph,i,visited):
                t = False
                break

    print("YES" if t else "NO")





