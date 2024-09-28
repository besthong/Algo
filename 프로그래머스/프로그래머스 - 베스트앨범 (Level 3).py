'''
dic 2개로 풀 수 있다.
dic -> genres의 총 판매량을 나타낸 딕셔너리
dics -> 각 판매량에 index값을 추가 한 딕셔너리
'''
def solution(genres, plays):
    answer = []
    dic ={}
    dics={}
    realans=[]
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
            dics[genres[i]].append((i,plays[i]))
        else:
            dic[genres[i]] = plays[i]
            dics[genres[i]] = [(i,plays[i])]
    print(dic.items())
    print(dics.items())

    dic = sorted(dic.items(), key = lambda x:x[1], reverse=True)
    print(dic)
    for i in dic:
        t = sorted(dics[i[0]], key = lambda x:x[1], reverse=True)
        print(t)
        answer.append(t[:2])
    print(answer)
    answer = sum(answer,[])
    for i in answer:
        realans.append(i[0])

    return realans


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres,plays))