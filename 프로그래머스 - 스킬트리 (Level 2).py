'''
for문 내 if 문으로 해결 가능했지만
내 케이스는 조금 복잡하게 구현되었다.
stack을 사용하려다 문자열 startswith 를 사용하여 풀었다.
'''
def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    temp=[]
    for i in skill_trees:
        i=list(i)
        strT=''
        for j in i:
            if j in skill:
                strT+=j
        temp.append("".join(list(strT)))

    for i in temp:
        if ''.join(skill).startswith(i):
            answer+=1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill,skill_trees))