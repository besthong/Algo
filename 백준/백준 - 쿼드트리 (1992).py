case = int(input())
temp = [list(map(int,input())) for _ in range(case)]
ans = []

def recur(case,x,y):
    color = temp[x][y]  #첫번째 컬러

    for i in range(x, x+case):
        for j in range(y, y+case):
            if color!=temp[i][j]:
                ans.append('(')
                recur(case//2,x,y)
                recur(case//2,x,y+case//2)
                recur(case//2,x+case//2,y)
                recur(case//2,x+case//2,y+case//2)
                ans.append(')')
                return

    if color == 0:
        ans.append(0)
    else:
        ans.append(1)
recur(case,0,0)
print(*ans,sep='')