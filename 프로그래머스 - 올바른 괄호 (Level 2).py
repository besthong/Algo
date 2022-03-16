'''
맨 처음, 스택만 사용하여 풀었으나
효율성 실패가 떴다. 이유는 s.pop(0) 하는 과정에서 O(n) 이기 때문에 숫자가 커질수록 비효율적이다
따라서 deque를 사용하여 O(1) 인 s.popleft()로 바꿔줬고, 통과했다. 나이쓰
'''

from collections import deque
def solution(s):
    s=deque(s)
    stack =[]

    while len(s)!=0:
        if len(stack)==0:
            stack.append(s.popleft())
        elif stack[-1]=='(' and s[0] == ')':
            stack.pop(-1)
            s.popleft()
        else:
            stack.append(s.popleft())

    if len(stack)==0:
        return True
    else:
        return False

s="()()"
s="(())()"
s=")()("
s="(()("
s=")"
print(solution(s))