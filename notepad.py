def solution(numbers):
    answer = ''
    answer = list(map(str,numbers))
    answer.sort(key=lambda x:x*3, reverse=True)
    return str(int("".join(answer)))


numbers=[6,10,2]
print(solution(numbers))