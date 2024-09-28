'''
어이없는 실수.
fail 값을 8로 고정시켜 자꾸 에러가 났다 하하
fail은 stages의 길이였는데..
또한 조건값 count==0일경우를 처리하지않아 런타임 에러가 났었다.
문제에서 스테이지에 도달한 유저가 없을경우는 해당 스테이지의 실패율을 0 으로 정의한다.
라는 조건값이 있었는데 못봤다..문제좀 제대로 읽자
'''
def solution(N, stages):
    answer = []
    stages=sorted(stages)
    fail = len(stages)
    for i in range(1,N+1):
        count = stages.count(i)
        if count == 0:
            answer.append((count,i))
        else:
            answer.append((count/fail,i))
            fail-=count

    answer=sorted(answer, key = lambda x:x[0] , reverse=True)
    for i in range(len(answer)):
        answer[i]=answer[i][1]

    return answer

N=5
stages=[1,2,2,1,3]
print(solution(N,stages))