# def can_cover_all_planks(A, B, C, mid):
#     # 현재 사용할 못 배열
#     nails = C[:mid]
#     nails.sort()  # 정렬된 못 배열
#
#     # 판자 커버 여부 확인
#     for start, end in zip(A, B):
#         if not any(start <= nail <= end for nail in nails):
#             return False
#     return True
#
#
# def solution(A, B, C):
#     N = len(A)
#     M = len(C)
#
#     C.sort()  # 못 배열 정렬
#
#     low, high = 1, M
#     answer = -1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if can_cover_all_planks(A, B, C, mid):
#             answer = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#
#     return answer

def check_plank(A, B, C, nails, mid):
    # 미드 값까지의 못으로 모든 플랭크가 고정되는지 확인하는 함수
    nailed = [False] * len(A)
    nail_positions = [0] * (2 * len(C) + 1)

    for i in range(mid + 1):
        nail_positions[C[i]] = 1

    for i in range(1, len(nail_positions)):
        nail_positions[i] += nail_positions[i - 1]

    for i in range(len(A)):
        if nail_positions[B[i]] - nail_positions[A[i] - 1] == 0:
            return False
    return True


def solution(A, B, C):
    # 플랭크와 못의 리스트가 주어졌을 때 최소한의 못을 찾는 함수
    N = len(A)
    M = len(C)

    result = -1
    low, high = 0, M - 1

    while low <= high:
        mid = (low + high) // 2
        if check_plank(A, B, C, M, mid):
            result = mid + 1
            high = mid - 1
        else:
            low = mid + 1

    return result

A=[1,4,5,8]
B=[4,5,9,10]
C=[4,6,7,10,2]

print(solution(A,B,C))