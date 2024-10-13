'''
이 문제는 슬라이딩윈도우를 사용해서 풀 수 있다.
처음에 슬라이딩윈도우인지 몰라서 그냥 dict에 넣고, 전부 포함이 됐을 때, end값을 통해 start값을 찾으려했다.
당연하게도 start값을 찾았어도, 최소값이 아닐 수 있기 때문에 틀렸다.

슬라이딩윈도우를 통해 end값, start값을 최신화 시키며, O(n) 만큼 반복하면 답을 찾을 수 있다.
'''
# def solution(gems):
#     type = list(set(gems))
#     dic = dict.fromkeys(type,0)
#     end=0
#     for i in range(len(gems)):
#         dic[gems[i]]+=1
#         if all(value >= 1 for value in dic.values()):
#             end=i+1
#             break
#
#     if end-len(type)==0:
#         start=1
#     else:
#         start=end-len(type)
#     answer=[start,end]
#
#     return answer

def solution(gems):
    types = len(set(gems)) #보서 종류 개수
    dic = {}
    answer=[0, len(gems)-1] #슬라이딩 윈도우를 위한 초기화
    start = 0 #start 0으로 초기화

    for end in range(len(gems)):
        dic[gems[end]]=dic.get(gems[end], 0) + 1 #데이터 있으면 gems[end] 반환하고, 없으면 0 반환 후 +1

        while len(dic) == types: #보석 전부 포함됐다면
            if end-start < answer[1] - answer[0]: #현재 구간의 길이가 지금까지 찾은 최소구간의길이 보다 작다면
                answer = [start,end] #최소구간길이를 업뎃한다

            dic[gems[start]] -= 1 #현재 보석의 값을 -= 1 해보고
            if dic[gems[start]]==0: #만약 값이 0이다?
                del dic[gems[start]] # 그럼 해당 보석을 dict에서 제거
            start+=1 #위완 상관없이 start를 +=1 해서 start를 업데이트 시킨다.

    return [answer[0]+1, answer[1]+1]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems=["AA", "AB", "AC", "AA", "AC"]
# gems=["A","A","A"]
print(solution(gems))