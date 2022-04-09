from collections import deque

# def solution(arr):
#     s = [arr.pop(0)]
#     while len(arr)!=0:
#         if s[-1]==arr[0]:
#             arr.pop(0)
#             continue
#         else:
#             s.append(arr.pop(0))
#     return s

def solution(arr):
    s = [arr.pop()]

    while len(arr)!=0:
        if s[-1] == arr[-1]:
            arr.pop()
            continue
        else:
            s.append(arr.pop())
    s=s[::-1]
    return s
arr = [1,1,3,3,0,1,1]
print(solution(arr))