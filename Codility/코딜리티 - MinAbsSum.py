def solution(A):
    total_sum = sum(abs(a) for a in A)
    n = len(A)

    # DP 배열 초기화 (총합의 절반까지만 계산)
    dp = [False] * (total_sum // 2 + 1)
    dp[0] = True  # 0은 항상 만들 수 있음

    # DP 업데이트 (가능한 부분합을 추적)
    for num in A:
        num = abs(num)
        for j in range(total_sum // 2, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    # 가능한 합 중에서 절반 이하의 최대 합을 찾기
    for i in range(total_sum // 2, -1, -1):
        if dp[i]:
            return total_sum - 2 * i


# 예제 사용
A = [1, 5, 2, -2]
print(solution(A))  # 결과: 0
