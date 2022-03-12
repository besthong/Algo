# DFS 사용
# def solution(numbers, target):
    # count=0
    # n=len(numbers)
    # def dfs(idx,result):
    #     if idx == n:
    #         if result == target:
    #             nonlocal count
    #             count+=1
    #         return
    #     else:
    #         dfs(idx+1,result+numbers[idx])
    #         dfs(idx+1,result-numbers[idx])
    # dfs(0,0)
    # return count


# product (중복순열) 사용
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum,product(*l)))
    return s.count(target)

# numbers = [1,1,1,1,1] ; target = 3
numbers=[4,1,2,1] ; target = 4
print(solution(numbers,target))

