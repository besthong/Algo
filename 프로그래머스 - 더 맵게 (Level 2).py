import heapq
def solution(scoville, k):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville)>=2:
        minimal = heapq.heappop(scoville) # 최소힙 루트값 가져온다 (가장작은값)
        if minimal >= k:                  # 최소힙 루트값이 K보다 작을경우는 모두 K보다 작을때
            return answer                 # 결과값 반환
        else:
            minimal+=heapq.heappop(scoville)*2
            heapq.heappush(scoville,minimal)
            answer+=1

    if scoville[0] < k:
        return -1
    else:
        return answer
# scoville = [1,2,3,9,10,12]
# k = 7

scoville = [1,2,3]
k = 11

print(solution(scoville,k))