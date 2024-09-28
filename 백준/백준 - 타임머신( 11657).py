'''
벨만포드 알고리즘 대표문제
1. a,b,c로 인접행렬 그래프를 만든 후
2. 그래프 V-1 개수만큼 반복하며 시작점부터 각 노드까지 그래프 최단거리 계산
3. 음의 cycle 있는지 검사 후, 사이클존재시 return false
'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []

#1. a,b,c 로 그래프 생성
for i in range(m):
    a,b,c = map(int,input().split())
    graph.append([a,b,c])

def bellmanFord(src):
    arr = [float('inf') for i in range(n+1)] #맨 처음 최대값 inf로 초기화
    arr[src] = 0

    for i in range(n-1):
        for a,b,c in graph:
            #현재 노드가 inf가 아니고 & 목표 거리까지의 경로 크기가 경유하는것보다 클 경우
            if arr[a]!=float('inf') and arr[b] > arr[a]+c:
                #테이블 갱신
                arr[b] = arr[a]+c

    #3. 음의사이클 확인 후 존재 시 return -1
    for a,b,c in graph:
        if arr[a]!=float('inf') and arr[b] > arr[a]+c:
            print(-1)
            return -1

    for i in range(2,len(arr)):
        if arr[i]==float('inf'):
            print(-1)
        else:
            print(arr[i])

bellmanFord(1)