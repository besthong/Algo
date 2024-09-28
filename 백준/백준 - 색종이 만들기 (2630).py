case = int(input())
temp = [list(map(int,input().split())) for _ in range(case)]
ans=[]
def recursion(case,x,y):
    color = temp[x][y]

    for i in range(x,x+case):
        for j in range(y,y+case):
            if temp[i][j]!=color:
                recursion(case//2,x,y)
                recursion(case//2,x,y+case//2)
                recursion(case//2,x+case//2,y)
                recursion(case//2,x+case//2,y+case//2)
                return

    if color==0:
        ans.append(0)
    else:
        ans.append(1)

recursion(case,0,0)
print(ans.count(0))
print(ans.count(1))

