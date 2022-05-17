'''
세가지 방법으로 해봤다.
첫번쨰가 내가 푼 방식 DP사용
두번째는 프로그래머스에 올라와있는 1등 코드
세번째는 이중반복문 사용하여 temp를 유지하며 같은 col 일때 0으로 치환하는 방식이다.
'''
import copy
def solution(land):
    answer = 0

    dp = copy.deepcopy(land)

    for index,i in enumerate(land):
        if index == 0:
            continue
        x = max(dp[index-1][1],dp[index-1][2],dp[index-1][3])
        dp[index][0] += x

        x = max(dp[index-1][0],dp[index-1][2],dp[index-1][3])
        dp[index][1] += x

        x = max(dp[index-1][0], dp[index-1][1], dp[index-1][3])
        dp[index][2] += x

        x = max(dp[index-1][0], dp[index-1][1], dp[index-1][2])
        dp[index][3] += x

    return max(dp[-1])
#
#
# def solution(land):
#     for i in range(1,len(land)):
#         for j in range(len(land[0])):
#             print(land[i-1][:j], land[i-1][j+1:])
#             print(land[i - 1][:j]+land[i - 1][j + 1:])
#             land[i][j] = max(land[i-1][:j] + land[i-1][j + 1:]) + land[i][j]
#             print()
#
#     print(land)

# import copy
# def solution(land):
#     size = 3
#
#     for i in range(1,size):
#         for j in range(4):
#             temp = copy.deepcopy(land[i-1])
#             temp[j] = 0
#             land[i][j] += max(temp)
#     print(*land, sep='\n')
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
