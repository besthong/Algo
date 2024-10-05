'''
해당 문제는 이중 우선순위큐로
매번 최소값,최대값을 가져와야한다.
따라서 나는 최대힙,최소힙을 사용하는 큐를 따로 만들어줬고, 각각의 delete 이벤트가 발생 시
min에서 삭제됐으면, max에서도 삭제하는 방식으로 풀었다.

'''

import heapq

def solution(operations):
    answer = []
    max_heap=[] #최대 힙
    min_heap=[] #최소 힙
    for op in operations:
        command,num = op.split(" ")
        num=int(num) #num은 정수형으로 변경
        if command =='I': # heappush
            heapq.heappush(max_heap, -num) #최대힙
            heapq.heappush(min_heap, num) #최소힙

        if command =="D" and num == -1: #최소값 추출
            if len(min_heap)==0: #최소힙 추출인데 힙이 비어있으면 break
                continue
            temp=heapq.heappop(min_heap) #최소 힙에서 데이터 추출
            max_heap.remove(-temp)  #최대힙에서 -으로 되어있는 num을 제거해주고
            heapq.heapify(max_heap) #최대힙 재작성

        if command == 'D' and num == 1: #최대갑 추출
            if len(max_heap)==0:
                continue
            temp=heapq.heappop(max_heap)
            min_heap.remove(-temp)
            heapq.heapify(min_heap)

    if len(max_heap)==0 or len(min_heap)==0:
        if len(max_heap)==0 and len(min_heap)!=0:
            ans=heapq.heappop(min_heap)
            return [ans,ans]
        if len(max_heap)!=0 and len(min_heap)==0:
            ans=heapq.heappop(max_heap)
            return [-ans,-ans]
        if len(max_heap)==0 and len(min_heap)==0:
            return [0,0]
    max_=heapq.heappop(max_heap)
    min_=heapq.heappop(min_heap)
    answer=[-max_,min_]
    return answer



op = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# op = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
op=["I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"]
print(solution(op))