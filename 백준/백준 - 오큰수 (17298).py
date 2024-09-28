case = int(input())
temp = list(map(int,input().split()))
ans=[-1]*case
stack = []

for i in range(len(temp)):
    while stack and temp[stack[-1]] < temp[i]:
        ans[stack.pop()] = temp[i]
    stack.append(i)
print(*ans)