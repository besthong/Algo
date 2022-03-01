case = input()
case=list(case+' ')
s=[]
temp = ''
for i in range(len(case)):
    if case[i].isdigit():
        temp+=case[i]
    elif case[i] == ' ':
        s.append(temp)
    else:
        s.append(temp)
        s.append(case[i])
        temp=''

for i in range(len(s)):
    if s[i] == '-':
        for j in range(i+1,len(s)):
            if s[j]=='+':
                s[j]='-'
    elif s[i]=='+':
        continue

    else:
        s[i]=int(s[i])

for i in range(1,len(s)):
    if s[i] == '-':
        s[i+1]=s[i-1] - s[i+1]
    elif s[i] == '+':
        s[i+1] = s[i-1] + s[i+1]

print(s[-1])

