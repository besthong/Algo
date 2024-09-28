'''
1. 이중리스트 board의 행,렬 변경 = list(zip(*board))
2. 반환값이 튜플이므로 list로 변환작업
3. 0을 제거하고, 역순

4. 나머지는 스택을 이용하여 같은값일때 pop해주는데 시간복잡도를 고려하여 deque 사용

1,2,3번을 한줄로 표현 할 수 있다.
------------------------------------------------------------------|
list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))|
------------------------------------------------------------------|
map,lambda,filter,zip을 적절히 사용함.
'''

from collections import deque
def solution(board, moves):
    answer = []
    board = list(zip(*board))
    board = [list(board[x]) for x in range(len(board))]

    for i in range(len(board)):
        answer.append([x for x in board[i] if x][::-1])

    stack = []
    for i in moves:
        if len(stack)==0:
            stack.append(answer[i-1].pop())
        elif len(stack)!=0 and len(answer[i-1])!=0:
            stack.append(answer[i-1].pop())

    temp=[]
    count=0
    stack=deque(stack)
    while len(stack)!=0:
        if len(temp)==0:
            temp.append(stack.popleft())
        elif stack[0]==temp[-1]:
            count+=2
            stack.popleft();temp.pop()
        else:
            temp.append(stack.popleft())
    return count

board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves= [1,5,3,5,1,2,1,4]
print(solution(board,moves))
