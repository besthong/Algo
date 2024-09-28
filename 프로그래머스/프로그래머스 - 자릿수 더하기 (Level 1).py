'''어렵지않게 풀이 가능'''
def solution(n):
    return sum(list(map(int,list(str(n)))))

n = 123
print(solution(n))