def solution(n):
    answer = []
    for i in range(n-1,1,-1):
        if n%i == 1:
            answer.append(i)
    return min(answer)


n = 1
print(solution(n))