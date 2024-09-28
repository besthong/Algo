'''
문제 자체는 어렵지 않지만
고려해야할 부분이 두가지 있다.

1. LRU 페이징 기법은 hit시 해당 값은 가장 최근 사용된것이므로 맨 뒤로 가야함.
2. 캐시사이즈가 0일때 [A,A] 라면 10이아닌 6을 출력함.

'''
from collections import deque
def solution(cacheSize, cities):
    answer = 0

    #리스트값 전부를 Upper
    cities = list(map(lambda x: x.upper(), cities))
    cities = deque(cities)

    hit=0
    miss=0

    stack = []

    while cities:
        # 1. 스택이 비어있거나, 캐시사이즈보다 작을때
        if len(stack)==0 or len(stack)<cacheSize:
            if cities[0] in stack:
                hit+=1
                stack.remove(cities[0])
                stack.append(cities.popleft())
            else:
                stack.append(cities.popleft())
                miss+=5

        # 2. 1번에의해 처음 값은 채워졌으나, 캐시사이즈가 0일경우 남아있는 캐시 초기화
        elif cacheSize == 0:
            stack.pop()

        # 3. 캐시사이즈보다 클 경우 작업
        else:
            if cities[0] in stack:
                hit+=1
                stack.remove(cities[0])
                stack.append(cities.popleft())

            else:
                miss+=5
                stack=stack[1:]
                stack.append(cities.popleft())

    answer = hit+miss
    return answer

cacheSize = 0
cities=["A","A"]
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize,cities))