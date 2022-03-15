# def solution(numbers):
#     answer = 0
#     numbers = list(map(str,numbers))
#     temp = sorted(numbers, key=lambda x:x*3, reverse=True)
#     print(temp)
#     numbers.sort(key=lambda x:x*3, reverse=True)
#     print(numbers)
#     return answer
import functools
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key = functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


numbers=[3,30,34,5,9]
numbers=[6,10,2]
print(solution(numbers))