'''
투포인트  start,end 값을 지정하여, 인덱스로만 접근하면 효율성 통과 가능
맨처음엔 스택,큐를 이용하여 실제 값 비교 +,- 작업을 했으나 실패

키포인트는 가장 몸무게가 적은 사람과, 몸무게가 많이 나가는 사람이 같이 못 탈 경우
몸무게가 많이 나가는 사람은 혼자 타야한다.

'''
def solution(people, limit):
    people = sorted(people)
    answer=0
    start = 0 ; end = len(people)-1

    while start<=end:
        answer+=1
        if people[start]+people[end] <= limit:
            start+=1; end-=1
        else:
            end-=1
    return answer


people = [100,500,500,900,950]
people = [40,40,40]
limit = 100

print(solution(people,limit))
