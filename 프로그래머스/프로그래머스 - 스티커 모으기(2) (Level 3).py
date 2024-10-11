'''
이 문제는 우선 주의해야할점이 원형이라는점이다.
그렇다고 모듈러연산으로 각 원소를 접근해야하는가?? 그건 아니고 단순하게 dp를 사용하면 된다.
한장을 떼면 양옆 두 장은 사용하지 못한다했으니 이동범위는 2씩 이동하게된다.
이는 dp[i]=max(dp[i-1], dp[i-2]+sticker[i]) 의 점화식으로 구현 가능하다.

그리고 조건이 한가지 더 있다.
첫번째 스티커를 선택하는경우의 dp와, 첫번째는 선택하지않고 두번째부터 선택하는 경우의 dp를 각각 구해
마지막에 max값을 리턴해주면 된다.
'''
def solution(sticker):
    answer = 0
    n=len(sticker)
    # 첫 번째 스티커를 선택하는 경우
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, n - 1):  # 마지막 스티커는 선택하지 않음
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

        # 첫 번째 스티커를 선택하지 않는 경우
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, n):  # 첫 번째 스티커는 선택하지 않음
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])


    return answer

sticker = [14, 6, 5, 11, 3, 9, 2, 10]
# sticker=[1,3,2,5,4]
print(solution(sticker))