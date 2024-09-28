'''
Dic를 사용하여 각 사용자가 몇번의 신고결과를 return 받았는지 저장한 후
list로 return

ps

report = {x : 0 for x in id_list}

dic 도 컴프리헨션 처럼 쓰기
'''

def solution(id_list,report,k):
    answer=[]
    report = list(set(report))

    dic={}
    dic2 = {}
    for i in id_list:
        dic[i]=0
        dic2[i]=0
    for i in report:
        a,b = i.split(' ')
        if b in dic.keys():
            dic[b]+=1

    for i in report:
        a,b = i.split(' ')
        if dic[b]>=k:
            dic2[a]+=1

    for k,v in dic2.items():
        answer.append(v)
    return answer
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

print(solution(id_list, report, k))
