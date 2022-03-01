from collections import deque

a,b = map(int,input().split()) # b=3
q = deque([i+1 for i in range(a)])
ans=[]
print('<',end='')
while q:
    for i in range(b-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(),end='')
    if q:
        print(', ',end='')
print('>')