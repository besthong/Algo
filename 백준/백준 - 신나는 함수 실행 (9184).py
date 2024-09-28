
def W(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return W(20,20,20)

    if temp[a][b][c]:
        return temp[a][b][c]

    if a<b<c:
        temp[a][b][c] = W(a,b,c-1) + W(a,b-1,c-1) - W(a,b-1,c)
    else:
        temp[a][b][c] = W(a-1,b,c) + W(a-1,b-1,c) + W(a-1,b,c-1) - W(a-1,b-1,c-1)

    return temp[a][b][c]


temp=[[[ 0 for i in range(21)] for i in range(21)] for i in range(21)]
while True:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    ans = W(a,b,c)
    print(f"w({a}, {b}, {c}) = {ans}")