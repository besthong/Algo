'''
문제의 관점을 달리해야함.
입국심사과정시 n=6; times=[7,10] return 28 인데
6번째 사람이 7 걸리는 사람에게 입국심사를 받게되면 28이 나오지만 (1초 기다린 후)
10 걸리는 사람에게 입국심사를 받으면 30이 걸린다.

이 복잡한 과정을 생각하기보다
이분탐색으로 최대 몇명이 심사를 받을 수 있는가를 생각 후
0~max(t)*n 0~60 중 몇명(mid)이 받을 수 있나를 생각해보자.
'''
def solution(n,t):
    start = 0; end = max(t)*n
    ans = 0
    while start<=end:
        mid = (start+end)//2
        temp = 0

        for i in range(len(t)):
            temp += mid//t[i] # mid 시간 내에 처리 가능한 최대 인원수

        if temp>=n: #처리 가능인원수가 널널할때가 end 범위 감소
            end = mid - 1
            ans = mid
        else:       # 처리 가능 인원수가 부족할때 start 범위 증
            start = mid + 1
    return ans

n=6; times=[7,10]
print(solution(n,times))
