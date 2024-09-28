import sys
case = int(input())

def VPS(vps):
    s = []
    while len(vps)!=0:
        if len(s)==0:
            s.append(vps[0])
            vps.pop(0)
        elif s[-1]=='(' and vps[0]==')':
            s.pop(-1)
            vps.pop(0)
        else:
            s.append(vps.pop(0))
    if len(s)!=0:
        print("NO")
    else:
        print("YES")
    return

for i in range(case):
    vps=sys.stdin.readline().rstrip()
    vps=list(vps)
    VPS(vps)