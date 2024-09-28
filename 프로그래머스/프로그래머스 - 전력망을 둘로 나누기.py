from collections import deque
def bfs(x,visited,graph):
    q = deque([x])
    visited[x] = True
    result = 1

    while q:
        cur = q.popleft()

        for i in graph[cur]:
            if visited[i] == False:
                result+=1
                q.append(i)
                visited[i]=True

    return result

def solution(n,wires):
    answer = n
    graph = [[]*n for _ in range(n+1)]

    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for i,j in wires:
        visited=[False]*(n+1)
        visited[j] = True
        result = bfs(i,visited,graph)
        print(result,end=' ')
        if abs(result-(n-result)) < answer:
            answer = abs(result-(n-result))
    return answer


# def bfs(x,visited,graph):
#     q = deque([x])
#     visited[x] = True
#     result = 1
#
#     while q:
#         cur = q.popleft()
#         for i in graph[cur]:
#             if visited[i] == False:
#                 result+=1
#                 q.append(i)
#                 visited[i] = True
#
#     return result
#
# def solution(n, wires):
#     answer = n
#     graph = [[] for _ in range(n+1)]
#
#     for a,b in wires:
#         graph[a].append(b)
#         graph[b].append(a)
#
#     for i,j in wires: # 1~9
#         visited =[False] *(n+1)
#         visited[j] = True
#         result = bfs(i,visited,graph)
#         if abs(result-(n-result)) < answer:
#             answer = abs(result-(n-result))
#     return answer


n=9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n,wires))