'''
다익스트라로 쉽게 해결 가능
실제 각 노드에 도착까지 최소비용을 구한 distance 리스트에서
주어진 K의 값보다 작은것들만 추출 후 len(list)

'''
import heapq

def solution(N, road, K):
    answer = 0

    INF = int(1e9)
    distance = [INF]*(N+1)
    graph = [[] for i in range(N+1)]

    for i in road:
        a,b,c = i[0],i[1],i[2]
        graph[a].append((b,c))
        graph[b].append((a,c))
    start = 1
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        cur_dis, cur_dst = heapq.heappop(q)

        if distance[cur_dst] < cur_dis:
            continue

        for next_dst, next_dis in graph[cur_dst]:
            totalDis = cur_dis + next_dis
            if distance[next_dst] > totalDis:
                distance[next_dst] = totalDis
                heapq.heappush(q,(totalDis,next_dst))

    distance=distance[1:]
    distance = [ i for i in distance if i <= K]
    return len(distance)


n = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
k = 3


n = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
k = 4


print(solution(n,road,k))