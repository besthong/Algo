import re
def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3 }
    option = {'':1, '*':2, '#':-1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    print(p)
    dart = p.findall(dartResult)
    print(dart)

    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2

        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


#아래가 굉장히 부끄러운 내 소스...
'''def solution(dartResult):
    answer = 0
    stack = []
    for i in list(dartResult):
        if i.isdigit() and not '0':
            stack.append(i)
        elif i == 'S':
            stack[-1] = int(stack[-1])**1
        elif i == 'D':
            stack[-1] = int(stack[-1])**2
        elif i == 'T':
            stack[-1] = int(stack[-1])**3
        elif i == '0':
            if len(stack)==0:
                stack.append(0)
            elif stack[-1] == '1':
                stack[-1] = int(stack[-1]+'0')
            else:
                stack.append(0)
        else:
            stack.append(i)

    temp=[]
    for i in map(str,stack):
        if i.isdigit():
            temp.append(i)
        elif i == '*':
            curLentemp = len(temp)
            if curLentemp<2: #1일경우
                temp[-1] = int(temp[-1])*2
            else:
                # answer += int(temp[-1])*2+int(temp[-2])*2
                temp[-1] = int(temp[-1])*2
                temp[-2] = int(temp[-2])*2

        elif i == '#':
            temp[-1] = int(temp[-1])*-1

    temp=map(int,temp)
    return sum(temp)
'''
dartResult = "1S2D*3T"
# dartResult = "1S*2T*3S"   # 1*2 *2 + 2^3 * 2 + 3^1
# dartResult = "1D2S#10S"
dartResult = "1D2S0T"
# dartResult = '0T1D2S'
print(solution(dartResult))
