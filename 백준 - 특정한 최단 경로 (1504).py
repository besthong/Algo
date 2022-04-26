'''
이 문제는 내 기준으로 생각해볼만한 부분이 두군데였다.
1. 방향성은 없지만 가중치는 존재하는 그래프
2. 경유를 해야만하는 정점2개

우선 1번의경우는 쉽게 해결 가능했던게, 주어진 a,b,c를 기준으로 두번 append를 진행해줬다.
2번의 경우는 간선이 두개뿐이라 v1먼저 갔을때, v2먼저 갔을때 각각 루트를 설정하여 다익스트라 알고리즘을 적용하여
풀 수 있었다.
'''

import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[]*m for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())

def dijkstra(start,end):
    dis = [float('inf')] * (n + 1)
    q=[]
    dis[start] = 0
    heapq.heappush(q,(dis[start],start))

    while q:
        cur_dis, cur_dst = heapq.heappop(q)

        if dis[cur_dst]< cur_dis:
            continue

        for next_dst, next_dis in graph[cur_dst]:
            totalDis = next_dis + cur_dis
            if dis[next_dst] > totalDis:
                dis[next_dst] = totalDis
                heapq.heappush(q,(totalDis, next_dst))
    return dis[end]

route1 = dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
route2 = dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)
minval = min(route1,route2)
if minval != float('inf'):
    print(minval)
else:
    print(-1)
