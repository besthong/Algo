from itertools import permutations

#효율성 제로 내풀이
def solution(n, k):
    answer = []

    arrN = [i+1 for i in range(n)]

    for i in enumerate(permutations(arrN,n)):
        print(i)
        if i[0]+1==k:
            answer.append(list(i[1]))
    answer=sum(answer,[])
    return answer

#아직 이해 반밖에 못한 남풀이
def solution(n,k):
    answer=[]
    people = [i+1 for i in range(n)]
    factorial=[]
    temp = 1
    for i in range(1,n):
        temp*=i
        factorial.append(temp)
    factorial=factorial[::-1]

    for d in factorial:
        q = (k-1) // d
        idx = q % len(people)

        answer.append(people.pop(idx))
    answer.extend(people)

    return answer

#남 풀이 2
from math import factorial
def solution(n, k):
    answer = []
    nums = list(range(1, n+1))
    order = []
    k -= 1
    for i in range(n-1, -1, -1):
        temp = factorial(i)
        q, r = divmod(k, temp)
        k = r
        order.append(q)
    # print(order)
    for idx in order:
        answer.append(nums.pop(idx))

    return answer
n=4
k=5
print(solution(n,k))