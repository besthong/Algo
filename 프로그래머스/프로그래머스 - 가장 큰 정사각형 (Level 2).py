'''
단순 반복문으로 푸려면 3중반복문이 사용되는데 효율성에서 바로 컷
dp 사용해야한다. 현재 i,j 값이 1일경우 i-1.j-1 j-1.j i,j-1 중 최소값 + 1 한게 최대 사각형의 길이가 된다.
이걸 생각해내기가 힘들어서 구글링의 도움을 받았다.
휴..
'''
def solution(board):
    answer = 0
    row,col = len(board),len(board[0])

    for i in range(1,row):
        for j in range(1,col):
            if board[i][j]==1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1

    max_=0
    for i in range(row):
        for j in range(col):
            if board[i][j]>max_:
                max_=board[i][j]
    return max_**2


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[0,0,1,1],[1,1,1,1]]
print(solution(board))