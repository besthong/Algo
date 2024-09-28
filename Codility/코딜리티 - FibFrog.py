'''
1. 피보나치 수열을 생성한다 len(A)의 길이보다 작을때까지만
2. BFS를 사용하여 A배열이 1일경우 즉, 개구리가 건너갈 수 있는 상황을 Q에 적재한다.
3. visited 리스트를 생성하여 개구리가 방문했는지를 표시한다. 이 리스트는 단순 0,1이 아닌 방문횟수까지 카운팅한다. A를 예로들면 [0,0,0,1,2,0,2,0,0,0,0]
4. 적재된 Q를 추출하여 현재 위치에서 개구리가 갈 수 있는 위치를 Q에 적재한다. 만약 이 때 다음포지션이 len(A)와 같다면, 현재위치의 방문값에 +1 후 리턴
5. 만약 아직 A의 길이보다 작다면, "A보다 작은지 & 다음 위치가 1인지 & 방문위치값이 -1 즉 방문한적없는지를 확인하고 맞다면 다음 q에 next_position을 append 후 현재 방문횟수값을 +1
'''

from collections import deque

def solution(A):
    if len(A)==0:
        return 1
    #피보나치 리스트 구하기 (A의 길이를 넘어설때까지)
    fibo=[1,2]
    while fibo[-1]<=len(A):
        fibo.append(fibo[-1]+fibo[-2])

    #BFS 사용

    visited = [-1]*(len(A)+1)
    q = deque([-1])
    visited[-1]=0


    while q:
        cur = q.popleft()
        cur_visited = visited[cur] #0

        for f in fibo:
            next_pos = cur+f
            if next_pos == len(A):
                return cur_visited + 1
            if next_pos <len(A) and A[next_pos] and visited[next_pos]==-1:
                visited[next_pos]=cur_visited+1
                q.append(next_pos)

    return -1

A=[0,0,0,1,1,0,1,0,0,0,0]
print(solution(A))