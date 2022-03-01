from collections import deque

case = int(input())
temp = [i+1 for i in range(case)]
q=deque(temp)

while True:
    if len(q)==1:
        print(str(list(q)[0]))
        break
    q.popleft()
    sec=q.popleft()
    q.append(sec)