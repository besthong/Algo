'''
모든 간선이 연결되어있어야하고(문제에서 연결이 안된 섬은 주어지지 않는다 하였으므로)
a->b 가 b->a와 같다 즉, 방향성이 없기때문에 그리디 알고리즘인 크루스칼 알고리즘을 사용하면 된다.
크루스칼 알고리즘의 핵심은
1. 비용순으로 오름차순
2. 부모 노드를 추적할 수 있도록 parent 배열을 만듦
3. 제일 적은 비용의 노드를 순환하면서 parent를 찾는다. -> 이유는 사이클이 생성되면 안되기때문, 만약 이을 때 같은 부모라면 싸이클이 생성되므로 pass한다.
4. 만약 부모가 같지 않다면 연결하여 같은 부모를 바라보게 한다 (union_find 함수 참조) & 비용을 더해주면 답이된다.
'''
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0

    parent = [i for i in range(n)]  # 부모 배열 초기화
    costs.sort(key=lambda x:x[2])

    for edge in costs:
        a,b,cost = edge

        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            answer+=cost

    return answer

n=4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))