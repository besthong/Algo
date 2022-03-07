from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

def bfs(start):
    count = 1
    q = deque([start])
    visited = [0 for _ in range(n+1)]
    visited[start] = 1

    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                count+=1
                q.append(i)
                visited[i] = 1
    return count
for i in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

realans=[]

maxV=0
for i in range(1,n+1):
    an = bfs(i)
    if an > maxV:
        maxV = an
    realans.append([i,an])

for i, an in realans:
    if an == maxV:
        print(i, end=' ')

'''dfs -> 메모리 초과'''
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
#
# n,m = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# count=0
# for i in range(m):
#     a,b = map(int,input().split())
#     graph[b].append(a)
#
# def dfs(graph,v,visited):
#     global count
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             count+=1
#             dfs(graph,i,visited)
#     return count
# realans = []
# visited = [False] * (n + 1)
# for i in range(1,n+1):
#
#     realans.append(dfs(graph,i,visited))
#     count=0
#
# max=realans[0]
# ans = []
# for i in range(len(realans)):
#     if realans[i] >= max:
#         ans.append(i+1)
#         max=realans[i]
#
# print(*ans)
