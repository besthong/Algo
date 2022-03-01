case = int(input())
s = []
for i in range(case):
    num = int(input())
    if num != 0:
        s.append(num)
    elif num==0:
        s.pop()
print(sum(s))