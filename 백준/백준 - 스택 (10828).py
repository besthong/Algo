import sys
case = int(input())
s=[]

for i in range(case):
    com = sys.stdin.readline().split()
    if com[0]=='push':
        s.append(com[1])
    elif com[0]=='pop':
        if len(s)!=0:
            print(s.pop())
        else:
            print('-1')
    elif com[0]=='size':
        print(len(s))
    elif com[0]=='empty':
        if len(s)==0: print('1')
        else: print('0')
    elif com[0]=='top':
        if len(s)!=0:
            print(s[-1])
        else:
            print('-1')