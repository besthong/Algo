'''
1,2,3을 뽑으나, 1,3,5 를 뽑으나 3개 부서에 준다는건 같다.
따라서 작은 순서대로 budget에서 빼보면서 음수가 되는 값이 최대 값이다.
'''
def solution(d,budget):
    answer = 0
    d.sort()
    for i in d:
        budget-=i
        if budget<0:
            break
        answer+=1
    return answer

'''첫 풀이 시간초과.. 당연하지만 한번 해봤다 d<=100'''
# from itertools import combinations
# def solution(d, budget):
#     answer = 0
#     arr=[]
#     for i in range(1,len(d)+1):
#         arr.append(list(combinations(d,i)))
#     for i in arr:
#         for j in i:
#             if sum(j)==budget:
#                 answer=len(j)
#     return answer

d = [1,3,2,5,4]
budget = 9

# d=[2,2,3,3]
# budget = 10

print(solution(d,budget))