n,b = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

def multiply(mA,mB):
    length = len(mA)
    dummy = [[0]*length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            for k in range(length):
                dummy[i][j] += mA[i][k]*mB[k][j]
            dummy[i][j]%=1000
    return dummy

def power(a,b):
    if b==1:
        for x in range(len(a)):
            for y in range(len(a)):
                a[x][y]%=1000
        return a
    else:
        temp=power(a,b//2)
        if b%2==0:
            return multiply(temp,temp)
        else:
            return multiply(multiply(temp,temp),a)

ans=power(a,b)
for i in range(n):
    for j in range(n):
        print(ans[i][j],end=' ')
    print()