'''
플로이드와샬 알고리즘 사용

1. 각 주어진 이긴 순위 정보 토대로 승패 관계 리스트 생성
2. a->b, b->c 인 경우 a->c 이므로 추가로 승패 작업 업데이트
3. 실제 자신을 제외한 모든 정점과 승패 유무를 알 수 있는 작업
4. n-1 번 진행한 정점만이 정확한 순위를 알 수 있다.
'''
def solution(n, results):
    realanswer = 0

    graph = [[float('inf')]*n for _ in range(n)]

    # 1. 각 주어진 이긴 순위 정보 토대로 승패 관계 리스트 생성
    for (a,b) in results:
        graph[a-1][b-1] = min(graph[a-1][b-1],1)

    # 2. a->b, b->c 인 경우 a->c 이므로 추가로 승패 작업 업데이트
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j]==1 or (graph[i][k]==1 and graph[k][j]==1):
                    graph[i][j] = 1

    # 3. 실제 자신을 제외한 모든 정점과 승패 유무를 알 수 있는 작업
    answer=[0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                answer[i]+=1
                answer[j]+=1

    # 4. n-1 번 진행한 정점만이 정확한 순위를 알 수 있다.
    for i in range(n):
        if answer[i]==n-1:
            realanswer+=1
    return realanswer
n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# results = [[1,4],[4,2],[2,5],[5,3]]
print(solution(n,results))
#return 2