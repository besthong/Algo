'''
맨 처음 문제가 복잡해보여 correct를 띄우기위해 O(n^2)으로 제출했다.
당연히 시간초과가 났고, correct는 맞길래 시간을 어떻게 단축 할 수 있을까 생각하다보니
O(nlog(n))으로 작동 할 수 있는 binary search를 적용하기로 했다.
mid값을 정하고, mid값을 level로 지정했을때, 해당값이 limit보다 작을경우, left = mid+1 아닐경우 right = mid-1
이렇게 풀면 통과 가능하다!!
'''
# def cal(diff,time_cur,time_prev,level): # 5,4,2,3
#     return (time_cur+time_prev)*(diff-level)+time_cur
#
# def solution(diffs, times, limit):
#     answer = 0
#     cnt=1 #level number
#
#     while cnt<=1000000:
#         limit_temp = limit
#         for i in range(len(diffs)):
#             if diffs[i]<=cnt: # level이 diff보다 높다면 limit에서 현재시간만큼 빼
#                 limit_temp -= times[i]
#             else:
#                 limit_temp -= cal(diffs[i],times[i],times[i-1],cnt)
#         if limit_temp<0:
#             cnt+=1
#         else:
#             return cnt
#
#     # return answer

def cal(diffs, times, level, limit):
    total_time = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            total_time += times[i]
        else:
            if i == 0:
                total_time += times[i] * (diffs[i] - level) + times[i]
            else:
                total_time += (times[i] + times[i-1]) * (diffs[i] - level) + times[i]
        if total_time > limit:
            return total_time
    return total_time

def solution(diffs, times, limit):
    left, right = 1, 100000
    while left < right:
        mid = (left + right) // 2
        if cal(diffs, times, mid, limit) > limit:
            left = mid + 1
        else:
            right = mid
    return left


diffs=[1,5,3]
times=[2,4,7]
limit=30

# diffs=[1,4,4,2]
# times=[6,3,8,2]
# limit=59
print(solution(diffs,times,limit))