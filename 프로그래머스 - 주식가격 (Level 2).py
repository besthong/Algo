def solution(p):
    ans = []

    for i in range(len(p)):
        count=0
        for j in range(i+1,len(p)):
            count += 1
            if p[i]>p[j]:
                break
        ans.append(count)
    return ans
p = [1,2,3,2,3]
print(solution(p))



''' 
이전 내 답
'''

def solution(prices):
    answer = []
    count=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            count+=1
            if prices[i]>prices[j]:
                break
        answer.append(count)
        count=0

    return answer