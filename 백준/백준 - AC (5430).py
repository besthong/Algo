import sys
input = lambda : sys.stdin.readline().strip()
case = int(input())

for i in range(case):
    com=input()
    length=int(input())
    temp=input()[1:-1].split(',')
    com=com.replace("RR","")

    r=0
    f,b=0,0

    for j in com:
        if j == 'R':
            r += 1
        elif j == 'D':
            if r % 2 == 0:
                f += 1
            else:
                b += 1
    if f+b<=length:
        temp=temp[f:length-b]

        if r % 2 == 1:
            print('['+','.join(temp[::-1])+']')
        else:
            print("["+",".join(temp)+"]")
    else:
        print('error')