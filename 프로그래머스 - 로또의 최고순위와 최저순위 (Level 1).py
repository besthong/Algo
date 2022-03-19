def solution(lottos, win_nums):
    answer = []
    ha = [6,6,5,4,3,2,1]
    suc=0
    fail=0
    zero = lottos.count(0)

    for i in range(6): #맞출 수 있는 최대
        if lottos[i] in win_nums:
            suc+=1
            fail+=1
    answer.append(ha[suc+zero])
    answer.append(ha[fail])
    return answer
lottos=[44,1,0,0,31,25]
win_nums=[31,10,45,1,6,19]

lottos=[0,0,0,0,0,0]
win_nums=[38,19,20,40,15,25]

lottos = [1,2,3,4,5,6]
win_nums=[7,8,9,10,11,12]
print(solution(lottos,win_nums))