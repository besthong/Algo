'''
기본 다익스트라 알고리즘 문제.
다익스트라는 인접행렬로 풀 경우 TimeComplexity O(V^2)이고, 인접리스트로 풀 경우 (ElogV)이므로
인접리스트로 풀자.
'''
import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())   # 정점, 간선개수
start = int(input())   # 스타트 정점

graph = [[]*n for _ in range(n+1)]
distance = [float('inf')]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        cur_dis,cur_dst = heapq.heappop(q)

        if distance[cur_dst] < cur_dis:
            continue

        for next_dst, next_dis in graph[cur_dst]:
            totalDis = cur_dis + next_dis
            if distance[next_dst] > totalDis:
                distance[next_dst] = totalDis
                heapq.heappush(q,(totalDis,next_dst))

    return distance

answer = dijkstra(start)
answer=answer[1:]
# print(*answer[1:],sep='\n')
for i in answer:
    if i == float('INF'):
        print('INF')
    else:
        print(i)