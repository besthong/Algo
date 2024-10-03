'''
Queen 조건 -> 대각선,수직,수평에 Queen을 놓을 수 없음
백트래킹 하면서 탈출하는 조건은 depth==N이다.
2차원 리스트가 아닌, 단일 리스트로 해결이 가능하다. 이유는 각 행에는 1개의 Queen만 적재 될 수 있기 때문이다.
근데 맨처음, 재귀를 사용해 백트래킹을 해서 제출했더니 마지막 테스트 케이스에서 시간초과가 발생했다.

구글링을해도 전부 dfs or recursion을 통한 풀이법만 있어서, gpt에 물어봤더니
비트마스킹으로 풀어낸 코드를 보여줬다.
아직도 이해가 안간다.. 일단 집가서 천천히 다시 따라가보자
'''
# def check(depth, board, n):
#     for i in range(depth):
#         # 같은 열에 있는지 또는 대각선에 있는지 확인
#         if board[i] == board[depth] or abs(depth - i) == abs(board[depth] - board[i]):
#             return False
#     return True
#
# def queen(n, depth, board, result):
#     if depth == n:  # 모든 퀸을 성공적으로 배치한 경우
#         result[0] += 1
#         return
#
#     for i in range(n):
#         board[depth] = i
#         if check(depth, board, n):
#             queen(n, depth + 1, board, result)
#
# def solution(n):
#     result = [0]  # 리스트를 사용하여 재귀 호출 시 값을 변경할 수 있도록 함
#     board = [0] * n
#     queen(n, 0, board, result)
#     return result[0]
#
#     return answer

def solution(n):
    def backtrack(row, cols, diagonals1, diagonals2):
        if row == n:
            return 1  # 하나의 유효한 배치를 찾았을 때
        count = 0
        # 현재 행에서 사용 가능한 모든 위치를 비트마스크로 계산
        available_positions = (~(cols | diagonals1 | diagonals2)) & ((1 << n) - 1)
        while available_positions:
            # 가장 오른쪽의 사용 가능한 위치 선택
            position = available_positions & -available_positions
            # 선택한 위치를 제외
            available_positions = available_positions - position
            # 재귀 호출: 다음 행으로 이동
            count += backtrack(row + 1,
                               cols | position,
                               (diagonals1 | position) << 1,
                               (diagonals2 | position) >> 1)
        return count

    return backtrack(0, 0, 0, 0)
n=4
print(solution(n))