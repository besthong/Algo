'''최소힙 사용'''
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
distance = [INF]*(n+1)

graph = [[] for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    #시작 노드
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        #가장 최단거리가 짧은 노드에 대한 정보 가져오기
        dist,now = heapq.heappop(q)

        # 이미 처리된 노드였으면 무시
        # 별도의 visit 테이블 필요 없이, 최단거리 테이블 이용하여 방문여부 확인
        if distance[now] < dist:
            continue
        #선택된 노드와 인접한 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            #선택된 노드를 거쳐 이동하는게 더 빠를때
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("도달불가")
    else:
        print(distance[i])


'''일반 노드 사용'''
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# n,m = map(int,input().split())
# start = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
#
# # 방문하지 않았고, 시작노드와 최단거리인 노드 반환
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1,n+1):
#         if not visited[i] and distance[i] < min_value:
#             min_value = distance[i]
#             index = i
#     return index
#
# # 다익스트라
# def dijkstra(start):
#
#     distance[start] = 0
#     visited[start] = True
#
#     for i in graph[start]:
#         distance[i[0]] = i[1]
#
#     for _ in range(n-1):
#         cur = get_smallest_node()
#         visited[cur] = True
#
#         for next in graph[cur]:
#             cost = distance[cur] + next[1]
#             if cost < distance[next[0]]:
#                 distance[next[0]] = cost
#
# dijkstra(start)
#
# for i in range(1,n+1):
#     if distance[i] == INF:
#         print("도달불가")
#     else:
#         print(distance[i])