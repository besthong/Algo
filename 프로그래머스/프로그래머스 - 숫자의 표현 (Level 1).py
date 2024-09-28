'''
이 문제는 두가지로 풀어봤다.
1,2 완전탐색과 3. 투포인터 알고리즘
완전탐색은 n^2의 알고리즘을 갖지만, 투포인터 알고리즘은 O(n)의 알고리즘을 가지기때문에 더 빠르다.

'''
# 1. 완전탐색 풀이 (시간초과 실패)
def solution(n):
    answer = 0
    # arr = [i for i in range(1,n+1)]

    cnt = 1
    while cnt<=n:
        # tempArr = arr[cnt:n]
        tempSum=0
        for i in range(cnt,n+1):
            tempSum+=i
            if tempSum >= n:
                if tempSum==n:
                    answer+=1
                    break
        cnt+=1
    return answer

# 2. 완전탐색 풀이 (시간초과 통과)
def solution(n):
    answer = 0

    for j in range(1,n+1):
        tempSum=0
        for i in range(j,n+1):
            tempSum+=i
            if tempSum == n:
                answer+=1
                break
            elif tempSum > n:
                break
    return answer


# 3. Two Pointer Algorithm O(n)
def solution(n):
    answer=0
    arr = [i for i in range(1,n+1)]
    print(arr)

    end = 0
    val = 0

    for start in range(n):
        while val < n and end < n:
            val += arr[end]
            end += 1
        if val == n:
            answer+=1
        val -= arr[start]
    return answer

n = 15
print(solution(n))
