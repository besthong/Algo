'''
그래프가 주어지고, 각 노드에 모두 방문하면서 가장 멀리있는 노드의 개수를 구하는 문제.
다익스트라로 구현이 가능하지만 간선 가중치가 없어서 BFS로 풀었다.
일반적인 BFS 모형을 취하되, 한번 들어간 큐 (첫번째 큐)가 끝날때마다 count하는식으로 for문을 사용해서 풀었으나
시간복잡도가 O(n^3)이 발생한다.

더 좋은 방법이 없나 검색하던도중, 다른사람의 코드를 참고하게되었는데
애초에 distance 리스트를 만들어 각 노드별 거리를 정의해두었다.
마지막으로는 가장 높은 숫자 개수를 출력하면 끝.
'''
from collections import deque

def solution(n,edge):
    graph = [ [] for _ in range(n+1)]
    dis = [ 0 for _ in range(n+1)]
    visited = [False]*(n+1)
    visited[1]=True

    for (a,b) in edge:
        graph[a].append(b)
        graph[b].append(a)

    q = deque([1])
    while q:
        cur = q.popleft()

        for j in graph[cur]:
            if not visited[j]:
                visited[j]=True
                q.append(j)
                dis[j]=dis[cur]+1

    print(dis)

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n,vertex))

# from collections import deque
#
# def solution(n, edge):
#     answer = 0
#
#     graph = [[]*(n) for _ in range(n+1)]
#
#     for i in edge:
#         a = i[0]
#         b=i[1]
#         graph[a].append(b)
#         graph[b].append(a)
#     q = deque([1])
#     visited=[False]*(n+1)
#     visited[1]=True
#
#     while q:
#         l=len(q)
#         for i in range(l):
#             cur = q.popleft()
#             for i in graph[cur]:
#                 if not visited[i]:
#                     q.append(i)
#                     visited[i]=True
#
#     return l
#
#
# n = 6
# vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
#
# print(solution(n,vertex))
