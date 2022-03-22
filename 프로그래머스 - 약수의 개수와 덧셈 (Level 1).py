def divisor(num):
    cnt = 0
    for i in range(1,num+1):
        if num%i == 0:
            cnt+=1
    return cnt
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        temp = divisor(i)
        if temp%2==0:
            answer+=i
        else:
            answer-=i

    return answer


left = 13
right = 17
print(solution(left,right))