case = int(input())

for i in range(case):
    temp = []
    dic = {}
    num = int(input())
    for j in range(num):
        temp.append(input().split()[1])
        if temp[j] in dic:
            dic[temp[j]]+=1
        else:
            dic[temp[j]] = 1
    ans = 1
    for value in dic.values():
        ans = ans*(value+1)
    print(ans-1)