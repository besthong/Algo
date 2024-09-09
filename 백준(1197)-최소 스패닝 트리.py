'''
3 3
1 2 1
2 3 2
1 3 3
'''

import sys
input=sys.stdin.readline

V,E = map(int,input().split())
parent=[0]*(V+1)

graph=[]
result=0

#부모 노드 찾기
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 부모노드 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#부모테이블 부모를 자기자신으로 초기화
for i in range(1,V+1):
    parent[i]=i

#정점,간선 설정
for _ in range(E):
    a,b,cost = map(int,input().split())
    graph.append((cost,a,b))

graph.sort()

for edge in graph:
    cost,a,b = edge
    #부모노드가 같지 않을경우에, 즉 사이클이 이뤄지지 않을때만
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)