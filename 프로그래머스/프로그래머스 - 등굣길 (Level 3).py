'''
이번 문제는 문제 분류 자체가 DP로 적혀있지 않았다면, BFS로 풀었을것같다.
지도가 나오고 경로가 나오니 바로 BFS라고 조건반사가 되어버렸다..

DP로 풀 때, puddles이 리스트이기때문에 미리 dp를 정해두고 puddles 항목마다 -1을 했다.
-1을 한 이유는 나중에 dp 반복할때, -1인 데이터는 0으로 치환하기위함이다.

또한 현재 m,n = [4,3] 으로 되어있는데, 3,4로 인식해야하므로 puddles와 dp에서 접근하는부분을 j,i로 변경했다.

일단 이 문제는 "가능한 경로의 개수"를 구하는것이라 DP를 사용하는게 맞다.
만약 "최단거리, 가장 적은 비용" 을 찾는 문제였다면 BFS로 푸는게 맞다.
'''
def solution(m, n, puddles):
    answer = 0
    #dp 초기화
    dp=[[0]*m for _ in range(n)]
    dp[0][0]=1

    for j,i in puddles:
        dp[i-1][j-1]=-1

    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:  # 웅덩이는 0으로 처리
                dp[i][j] = 0
                continue
            if i == 0 and j > 0:  # 첫 번째 행 처리
                dp[i][j] = dp[i][j - 1]
            elif j == 0 and i > 0:  # 첫 번째 열 처리
                dp[i][j] = dp[i - 1][j]
            elif i > 0 and j > 0:  # 나머지 일반 케이스
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007  # 값이 커질 수 있으므로 모듈러 연산

    return dp[n-1][m-1]

m=4
n=3
puddles=[[2,2]]
print(solution(m,n,puddles))