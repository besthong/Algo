case = int(input())
temp = [list(map(int,input().split())) for _ in range(case)]
ans=[]
def recursion(case,x,y):
    color = temp[x][y]
    for i in range(x,x+case):
        for j in range(y,y+case):
            if color != temp[i][j]:
                recursion(case//3, x, y)    #(0,0)

                recursion(case//3,x+case//3,y)  #(3,0)
                recursion(case//3,x+(case//3)*2,y) #(6,0)

                recursion(case//3, x,y+case//3) #(0,3)
                recursion(case//3, x, y+(case//3)*2) #(0,6)

                recursion(case//3, x+case//3, y+case//3) #(3,3)
                recursion(case//3, x+(case//3)*2, y+case//3) #(6,3)

                recursion(case//3, x+case//3, y+(case//3)*2) #(3,6)
                recursion(case//3, x+(case//3)*2, y+(case//3)*2) #(6,6)
                return

    if color==-1:
        ans.append(-1)
    elif color == 0:
        ans.append(0)
    else:
        ans.append(1)

recursion(case,0,0)
print(ans.count(-1))
print(ans.count(0))
print(ans.count(1))

