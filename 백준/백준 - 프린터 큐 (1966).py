case = int(input())
for i in range(case):
    a,b = map(int,input().split())
    temp = list(map(int,input().split()))
    priority = [-1]*len(temp)
    priority[b] = 'target'
    answer=0

    while True:
        if temp[0]==max(temp):
            answer+=1

            if priority[0]=='target':
                print(answer)
                break
            else:
                temp.pop(0)
                priority.pop(0)
        else:
            temp.append(temp.pop(0))
            priority.append(priority.pop(0))