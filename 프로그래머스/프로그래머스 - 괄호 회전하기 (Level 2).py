'''
어렵지 않은 문제이나, 리스트의 복사 과정에서 좀 시간이 걸렸다.
s로 받은 리스트를 직접 제거하다보니 파라미터를 전달한 solution 함수에서도 리스트가 제거되어 에러가 발생했다.
얕은복사(copy) 를 사용해서 풀었는데
얇은복사도 필요없는 s를 건들지 않는 반복문이 있다. (1-1)
'''

from collections import deque
import copy
'''내 함'''
def isCorrect(s):
    dic = { '(':')',
            '[':']',
            '{':'}',
            '}':'}',
            ']':']',
            ')':')'}
    temp=copy.copy(s)
    stack=[]

    while len(temp)!=0:
        if len(stack)==0:
            stack.append(temp.popleft())
        elif dic[stack[-1]] == temp[0]:
            stack.pop()
            temp.popleft()
        else:
            stack.append(temp.popleft())
    if len(stack)==0:
        return True
    else:
        return False

'''리스트 s를 건들지 않는 참고 함수'''
def check(s):
    pair = {
    '(' : ')',
    '[' : ']',
    '{' : '}'}

    st = []
    for e in s:
        if not st:
            st.append(e)
            continue
        if st[-1] in pair and pair[st[-1]]==e:
            st.pop()
        else:
            st.append(e)
    return not st

def solution(s):
    answer = 0
    # s=list(s)
    s=deque(s)
    for i in range(len(s)):
        if isCorrect(s):
            answer+=1
        s.append(s.popleft())
    return answer

s = "[](){}"
s = "}]()[{"
s = "[)(]"
s = "}}}"
print(solution(s))

