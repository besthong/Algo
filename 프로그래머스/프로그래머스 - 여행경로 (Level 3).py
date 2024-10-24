'''
이번 문제는 깊이우선탐색으로 풀면 된다.
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]의 값을
인접리스트를 사용하여
{"INC":["JFK"],"HND":["IAD"]} 와 같은 형태로 변경 후 INC부터 시작이므로 dfs를 실행하면 된다.
defaultdict를 사용하여 기본값을 list로 정의함과 동시에
graph[start]에 접근 될 때 list를 생성하여 .append(end)를 하면 위와 같은 형태로 초기화 할 수 있다.
'''
from collections import defaultdict

def dfs(graph,cur,visited):
    while graph[cur]:
        next_ = graph[cur].pop(0)
        dfs(graph,next_,visited)

    visited.append(cur)

def solution(tickets):
    answer = []
    graph=defaultdict(list)
    visited = []
    print(graph)
    for start,end in tickets:
        graph[start].append(end)

    for key in graph:
        graph[key].sort()

    dfs(graph,"ICN",visited)
    visited=visited[::-1]
    return visited

tickets=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets =[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))