#fibo 0과 1 몇번씩 출력되는지

case = int(input())

def fibo(num):
    if num == 0:
        print("1 0")
        return
    elif num==1:
        print("0 1")
        return

    temp=[0]*num
    temp[0]=0; temp[1]=1

    for i in range(2,num):
        temp[i] = temp[i-1]+temp[i-2]
    print(temp[-1],temp[-1]+temp[num-2])

for _ in range(case):
    i = int(input())
    fibo(i)

