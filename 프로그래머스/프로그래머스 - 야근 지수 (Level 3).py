'''
해당 문제는 힙을 사용하면 쉽게 풀 수 있다.
파이썬은 heapq 모듈을 제공해주기떄문에 더 쉬울 수 있다.
요구사항: works 배열이 주어졌을때, n만큼 야근을 할 수 있다면, 가장 최소로 피로도를 찾는방법이다
한마디로 works 배열 중 가장 큰 값을 -1 하면서 줄여나가면 된다.
heapq는 최소힙을 보장하기때문에 최대힙으로 만드려면 트릭이 필요한데
마이너스 성질을 사용하여 -num 을 push 해준다면 맨 앞으로 오게되어있다.
따라서 문제 요건에 맞춰 작성하면 된다.
'''
import heapq

def solution(n, works):
    answer = 0
    heap=[]
    for i in works:
        heapq.heappush(heap,-i)

    for i in range(n):
        temp = -heapq.heappop(heap) #최대값 추출
        temp-=1
        # heapq.heapify(heap)
        heapq.heappush(heap,-temp)
    answer=sum([(-i)**2 for i in heap])

    if sum(works)<=n:
        return 0
    return answer


works=[4,3,3]
n=4
works=[2,1,2]
n=1
works=[1,1]
n=3
print(solution(n,works))