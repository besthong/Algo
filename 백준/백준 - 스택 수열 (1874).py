case = int(input())
stack=[]
num = [int(input()) for _ in range(case)]
count = 0
ans=[]
for k in range(0,case):
    for i in range(count,num[0]):
        count+=1
        stack.append(count)
        ans.append("+")
    if stack[-1]==num[0]:
        stack.pop()
        ans.append("-")
        num.pop(0)

if len(stack)==0:
    print(*ans, sep='\n')
else:
    print("NO")