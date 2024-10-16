'''
이 문제는 3개로 나눠서 풀었다.
1. 단순 슬라이딩 윈도우
2. 이진탐색
3. 슬라이딩윈도우 (deque)사용

2,3은 통과가 되지만, 1번은 통과가 되지않는다.
1번 코드의 경우 O(n*k)가 되는데, 효율성에서 전부 시간초과가 발생했다.
슬라이딩 윈도우와 가장 비슷한 이진 탐색을 생각해보자.
우선 mid값을 정해준다 (start=1, end=max(stones)) 그럼 초기값은 1,5 mid는 6//2 즉 3이 된다.
3명이 넘어갈 수 있는지를 검사하면 된다.(can_cross 함수 참조)

그럼 슬라이딩 윈도우로 풀 수 없을까?? GPT의 도움을 받아봤다
deque를 사용하면 슬라이딩 윈도우를 사용해서 풀 수 있으며, O(n)까지 줄일 수 있다.
deque를 사용함으로써 매번 윈도우의 모든 요소를 다시 계산하지않고, 윈도우 이동에 맞춰 계산을 업데이트 하는 방법이다.
'''

#-------------단순 슬라이딩 윈도우 풀이-----------
# def solution(stones, k):
#     max_in_windows = []  # 각 윈도우 내에서 최대값을 저장할 리스트
#
#     # 슬라이딩 윈도우로 최대값을 구하는 과정
#     for i in range(len(stones) - k + 1):
#         window_max = max(stones[i:i + k])  # 윈도우 내의 최대값
#         max_in_windows.append(window_max)
#     print(max_in_windows)
#     # 윈도우 최대값들 중 최소값이 답이 됨
#     return min(max_in_windows)


#-------------이진탐색 풀이-------------------
# def can_cross(stones, k, mid):
#     # 연속된 '0 이하의 값'이 k개 이상이면 건널 수 없음
#     skip = 0
#     for stone in stones:
#         if stone < mid:
#             skip += 1
#             if skip >= k:  # 연속된 돌이 k개 이상이면 건널 수 없음
#                 return False
#         else:
#             skip = 0  # 건널 수 있는 돌이 나오면 다시 0으로 초기화
#     return True  # 끝까지 건널 수 있음
#
#

# def solution(stones, k):
#     # 이진 탐색 범위는 1명부터 max(stones)명까지
#     left, right = 1, max(stones)
#
#     while left <= right:
#         mid = (left + right) // 2  # 중간값 설정
#         if can_cross(stones, k, mid):
#             left = mid + 1  # 더 많은 인원도 건널 수 있는지 확인
#         else:
#             right = mid - 1  # 더 적은 인원만 건널 수 있음
#
#     return right  # 최대 건널 수 있는 인원을 반환


#-------------deque를 사용한 슬라이딩 윈도우 풀이-----------
from collections import deque


def solution(stones, k):
    deque_window = deque()
    result = []

    for i in range(len(stones)):
        # 덱에서 윈도우 바깥에 있는 값 제거
        if deque_window and deque_window[0] == i - k:
            deque_window.popleft()

        # 덱에서 현재 값보다 작은 값 제거
        while deque_window and stones[deque_window[-1]] < stones[i]:
            deque_window.pop()

        # 덱에 현재 인덱스 추가
        deque_window.append(i)

        # 결과에 현재 윈도우의 최대값 추가 (첫 윈도우부터)
        if i >= k - 1:
            result.append(stones[deque_window[0]])

    return min(result)


# 예시 실행
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))  # 결과: 3
