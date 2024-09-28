case = int(input())
dis = list(map(int,input().rstrip().split()))
oil = list(map(int,input().rstrip().split()))

minVal = oil[0]
sum = 0
for i in range(case-1):
    if minVal > oil[i]:
        minVal = oil[i]
    sum+=(minVal * dis[i])
print(sum)