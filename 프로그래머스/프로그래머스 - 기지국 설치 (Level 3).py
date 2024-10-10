'''
주석처리 된 내 방법으로 풀게되면 답은 맞으나 시간초과가 발생한다.
n이 최대 2억개 이므로 그럴만하다.
따라서 수학적 사고가 필요하다.
먼저 시작범위와 끝범위를 업데이트 하면서 커버가 필요한 집의 개수를 구하고
2*n+1 만큼 이동해서 실제 필요한 안테나의 개수를 answer에 계속 더해주면 된다.
'''
# def solution(n, stations, w):
#     answer = 0
#     #초기 기지국이 설치되어있는 만큼 표시
#     visited=[False]*n
#     for i in stations:
#         left=max(0,i-w-1)
#         right=min(n-1,i+w-1)
#
#         for i in range(left,right+1):
#             visited[i]=True
#
#     i=0
#     while i<n:
#         if not visited[i]:
#             answer+=1
#             i+=(w*2+1)
#         else:
#             i+=1
#     return answer

def solution(n, stations, w):
    answer = 0
    # 이전 기지국의 끝 범위
    previous_end = 0

    for station in stations:
        # 현재 기지국의 시작 범위
        current_start = station - w
        # 기지국이 커버하지 않는 집의 시작 위치
        if current_start > previous_end + 1:
            # 커버되지 않는 집의 수를 계산합니다.
            uncovered_houses = current_start - (previous_end + 1)
            # 필요한 기지국 개수를 계산합니다.
            coverage = 2 * w + 1  # 한 기지국이 커버하는 집의 수
            needed_stations = (uncovered_houses + coverage - 1) // coverage
            answer += needed_stations

        # 현재 기지국의 끝 범위를 업데이트합니다.
        previous_end = station + w

    # 마지막 기지국 이후에 커버되지 않는 집이 있는지 체크합니다.
    if previous_end < n:
        uncovered_houses = n - previous_end
        coverage = 2 * w + 1
        needed_stations = (uncovered_houses + coverage - 1) // coverage
        answer += needed_stations

    return answer



# 예시 사용
n = 11  # 총 구역 수
stations = [4, 9]  # 안테나 위치
w = 1  # 커버 범위
print(solution(n, stations, w))  # 결과 출력
