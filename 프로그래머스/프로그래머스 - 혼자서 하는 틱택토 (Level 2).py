'''
이번 문제는 다 풀고, 몇몇 테스트케이스에서 계속 실패해서 시간이 좀 걸렸다.
결과적으로 문제는 "동시에 승리했을 경우"를 생각하면 된다.
따라서 check_winner를 통해 두명의 결과값을 반환하게되고 만약 동시에 승리하게되면
False 를 반환하도록 코드를 변경했더니 통과했다
'''
from collections import Counter

def check_winner(board):
    x_wins = False
    o_wins = False
    win_positions = []

    # 가로 검사
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '.':
            if board[i][0] == 'X':
                x_wins = True
            else:
                o_wins = True

    # 세로 검사
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '.':
            if board[0][i] == 'X':
                x_wins = True
            else:
                o_wins = True

    # 대각선 검사
    if board[0][0] == board[1][1] == board[2][2] != '.':
        if board[0][0] == 'X':
            x_wins = True
        else:
            o_wins = True
    if board[0][2] == board[1][1] == board[2][0] != '.':
        if board[0][2] == 'X':
            x_wins = True
        else:
            o_wins = True

    return x_wins, o_wins

def solution(board):
    ans = ''.join(board)
    cnt = Counter(ans)

    # 총 수의 개수 확인
    if cnt['O'] < cnt['X'] or cnt['O'] - cnt['X'] > 1:
        return 0  # 불가능한 경우

    x_wins, o_wins = check_winner(board)

    # 두 명이 동시에 승리한 경우
    if x_wins and o_wins:
        return 0

    # 승자가 있는 경우
    if o_wins:
        if cnt['O'] == cnt['X'] + 1:
            return 1
        else:
            return 0
    if x_wins:
        if cnt['O'] == cnt['X']:
            return 1
        else:
            return 0

    # 승자가 없는 경우
    if cnt['O'] + cnt['X'] == 9 or cnt['O'] == cnt['X'] + 1 or cnt['O'] == cnt['X']:
        return 1
    else:
        return 0


board=["O.X", ".O.", "..X"]
board=["OOO", "...", "XXX"]
# board=["OXX", "O..", "O.."]
# board=["...", "...", "..."]
# board=["XXO", ".OX", "O.."]
# board=["OOO", "O..", "XXX"]
board=["OXO","XOX","OXO"]
print(solution(board))