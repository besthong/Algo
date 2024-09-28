case = int(input())

for num in range(case):
    a = int(input())
    if a == 1 or a== 2 or a == 3:
        print(1)
    else:
        temp = [0] * a
        temp[0] = temp[1] = temp[2] = 1
        for i in range(3,a):
            temp[i] = temp[i-2]+temp[i-3]
        print(temp[-1])