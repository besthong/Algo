'''
BFS로 풀었으나 맨처음 Visited=[] 로 만들어 조건값 검사를 in 으로 했다 -> 시간초과
그래서 visited=set() 로 만들어 중복값을 제거했다. -> 메모리 초과
검색좀 해보니 값이 10^5 이상일경우 데이터가 필요없어서
데이터 조건값을 0 < target < 100000 으로 정했더니 통과했다.
아오 머리야
'''
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
if n==k:
    print(0)
    quit()
visited = set()

def bfs(n):
    q = deque()
    q.append((n,0))

    while q:
        cur,count = q.popleft()
        arr = [cur*2, cur+1, cur-1]
        for i in arr:
            if i == k:
                print(count+1)
                quit()
            if i in visited or i < 0 or i>100000:
                continue
            else:
                q.append((i,count+1))
                visited.add(i)
bfs(n)
