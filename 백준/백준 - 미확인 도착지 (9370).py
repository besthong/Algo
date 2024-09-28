'''
다익스트라 구현은 쉬웠지만, 시간초과때문에 고생한문제
맨처음 코드는 다익스트라를 6번 계산하도록 해서 시간초과가 발생하였고,
각 dijkstra(s),g,h 로 3번 돌린 후
배열로 각 거리 계산의 합이 목적지까지의 합과 같을경우에 (최단거리) answer에 append 하였다.
'''

import heapq
def dijkstra(start):
    q=[]
    dis = [int(1e9)] * (n + 1)
    dis[start] = 0
    heapq.heappush(q,(dis[start],start))

    while q:
        cur_dis, cur_dst = heapq.heappop(q) # 현재 정점, 현재 간선 가중치
        if dis[cur_dst] < cur_dis:
            continue

        for next_dst,next_dis in graph[cur_dst]:
            totalDis = next_dis+cur_dis
            if dis[next_dst] > totalDis:
                dis[next_dst] = totalDis
                heapq.heappush(q,(totalDis,next_dst))

    return dis

T = int(input()) # Total case
for _ in range(T):
    answer = []
    n,m,t = map(int,input().split()) # n: 정점, m: 간선, t: 도착지후보
    s,g,h = map(int,input().split()) # s: 출발지, g,h : g<->h 정점의 도로를 지나갔다.
    graph = [[]*(n) for _ in range(n+1)]

    destination=[]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    dst_s=dijkstra(s)
    dst_g=dijkstra(g)
    dst_h=dijkstra(h)

    for i in range(t):
        temp = int(input())
        if dst_s[g]+dst_g[h]+dst_h[temp] == dst_s[temp] or dst_s[h]+dst_h[g]+dst_g[temp] == dst_s[temp]:
            answer.append(temp)

    print(*sorted(answer))



        # if allDis[temp]<allDis[temp]+
#아래 해당 코드는 시간초과
# import heapq
# def dijkstra(start,end):
#     q=[]
#     dis = [float('inf')] * (n + 1)
#     dis[start] = 0
#     heapq.heappush(q,(dis[start],start))
#
#     while q:
#         cur_dis, cur_dst = heapq.heappop(q) # 현재 정점, 현재 간선 가중치
#         if dis[cur_dst] < cur_dis:
#             continue
#
#         for next_dst,next_dis in graph[cur_dst]:
#             totalDis = next_dis+cur_dis
#             if dis[next_dst] > totalDis:
#                 dis[next_dst] = totalDis
#                 heapq.heappush(q,(totalDis,next_dst))
#
#     return dis[end]
#
#
# T = int(input()) # Total case
# for _ in range(T):
#     answer = []
#     n,m,t = map(int,input().split()) # n: 정점, m: 간선, t: 도착지후보
#     s,g,h = map(int,input().split()) # s: 출발지, g,h : g<->h 정점의 도로를 지나갔다.
#     graph = [[]*(n) for _ in range(n+1)]
#
#     destination=[]
#     for _ in range(m):
#         a,b,c = map(int,input().split())
#         graph[a].append((b,c))
#         graph[b].append((a,c))
#
#     for i in range(t):
#         temp = int(input())
#         originShortestDis = dijkstra(s,temp) # 기존 시작정점부터 목적지까지의 최단거리
#         destination.append([temp,originShortestDis])
#         route1 = dijkstra(s,g)+dijkstra(g,h)+dijkstra(h,temp)
#         route2 = dijkstra(s,h)+dijkstra(h,g)+dijkstra(g,temp)
#         min_route = min(route1,route2)
#         if min_route > destination[i][1]:
#             continue
#         else:
#             answer.append(destination[i][0])
#
#     answer =" ".join(map(str,sorted(answer)))
#     print(answer)


