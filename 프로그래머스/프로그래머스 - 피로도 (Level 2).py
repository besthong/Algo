'''
정렬로 풀어보고자 했으나, 0열 기준, 1열기준 둘다 값이 안나와서
완전탐색으로 진행했으며
Permutations (순열) 을 사용했다.
'''
from itertools import permutations
def solution(k, dungeons):
    answer = []

    d = list((permutations(dungeons,len(dungeons))))
    for i in d:
        temp = k
        count = 0
        for j in i:
            if j[0]<=temp: # 던전의 최소피로도가 같거나 작을때
                count+=1
                temp-=j[1]
        answer.append(count)
    return max(answer)
k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k,dungeons))
