N = int(input())

if N==1:
    print(1)
else:
    temp=[0]*N
    temp[0]=1
    temp[1]=2
    for i in range(2,N):
        temp[i]=(temp[i-1]+temp[i-2])%15746

    print(temp[-1])