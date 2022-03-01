'''
입출력 그냥 input() 했다가 시간초과..
readline으로 바꿨다.
'''
from collections import deque
import sys
case = int(sys.stdin.readline())
q=deque([])
for i in range(case):
    com=list(sys.stdin.readline().split())
    if com[0]=='push_front':
        q.appendleft(com[1])
    elif com[0]=='push_back':
        q.append(com[1])
    elif com[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif com[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)

