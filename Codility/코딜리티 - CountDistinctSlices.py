'''
해당 문제는 맨 처음 슬라이딩 윈도를 통해 풀었다가, index 에러가 발생해서 문제 접근을 다시해야했다.
검색을 조금 해봤는데 각 인덱스마다 가능한 개수를 지정하고 숫자 카운팅 리스트(여기선 defaultdict)를 이용했다.
ex. A=[3,4,5,5,2] 라면 3 부터 시작하며 가능한 index값을 dict에 추가하고 +1로 표시했다
따라서 3:1, 4:1, 5:1이 되고 각각 자신일때의 3개와 3-4, 3-4-5, 4-5 까지 cnt가 처음 6개가 만들어진다.
다시 5가 나왔을때는 이미 5:1이므로 중복이라고 판단이 되며, 이 때는 start를 늘리면 된다.
-> O(n)
'''
# from collections import deque
# def is_same(q):
#     if len(q) == len(list(set(q))):
#         return True
#     else:
#         return False
#
# def solution(M,A):
#     start,end = 0,1
#     cnt=len(A)
#     q=deque()
#     q.append(A[start])
#     while end<=len(A):
#         q.append(A[end])
#         if is_same(q):
#             # q.append(A[end])
#             end+=1
#             cnt+=1
#         else:
#             q=[]
#             start+=1
#             end=start+1
#             q.append(A[start])
#
#     return cnt

from collections import defaultdict
def solution(M,A):
    start=0;end=0;cnt=0
    freq = defaultdict(int)

    while end<len(A):
        while end<len(A) and freq[A[end]]==0:
            freq[A[end]]+=1
            end+=1
            cnt += end-start
        if end<len(A):
            freq[A[start]] -= 1
            start+=1

    if cnt > 1000000000:
        return 1000000000
    else:
        return cnt

A=[3,4,5,5,2]
M=6
print(solution(M,A))