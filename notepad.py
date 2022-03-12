def solution(n, t):
    start = 0
    end = max(t)*n
    ans=0
    while start<=end:
        mid = (start + end) // 2
        temp = 0
        for i in range(len(t)):
            temp += mid//t[i]

        if temp >= n:           # 시간이 여유로운경우 (더 많은 사람을 처리할수있을경우)
            end = mid - 1
            ans=mid
        else:
            start = mid + 1
    return ans

n = 6
times = [7,10]
print(solution(n,times))