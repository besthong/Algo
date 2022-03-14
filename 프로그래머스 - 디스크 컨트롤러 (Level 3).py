'''
heap 사용하자
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[100, 100], [1000, 1000]]), 500)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
'''

# import heapq
#
# def solution(jobs):
#     jobs = [list(reversed(x)) for x in jobs]
#     heapq.heapify(jobs)
#     ans = []
#     temp= []
#     while len(jobs)!=0:
#         if len(ans)==0:
#             ans.append(jobs[0][0]-jobs[0][1])
#             temp.append(jobs[0][1])
#             heapq.heappop(jobs)
#         else:
#             ans.append(ans[-1]+jobs[0][0])
#             temp.append(jobs[0][1])
#             heapq.heappop(jobs)
#
#     ans=[ans[i]-temp[i] for i in range(len(ans))]
#     return int(sum(ans)//len(ans))
#
# # jobs = [[0, 3], [1, 9], [2, 6]]
#
# jobs = [[0, 6], [0, 8], [7, 1]]
# print(solution(jobs))

import heapq
def solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1],j[0]])

        if len(heap)>0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i+=1
        else:
            now +=1
    return answer//len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))