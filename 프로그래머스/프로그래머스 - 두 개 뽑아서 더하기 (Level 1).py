from itertools import combinations
def solution(numbers):

    numbers = set(list(combinations(numbers,2)))

    answer = []
    for i in numbers:
        total = sum(i)
        if total not in answer:
            answer.append(total)
    answer.sort()
    return answer



numbers = [2,1,3,4,1]
numbers = [5,0,2,7]
print(solution(numbers))