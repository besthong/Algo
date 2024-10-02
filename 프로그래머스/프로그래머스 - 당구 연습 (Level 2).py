'''
당구대를 생각하면서 풀어보면 되는데, 각 상 하 좌 우 쿠션에 닿는걸 생각해야한다.
네가지 중 최소값을 찾으면 된다 근데 이 때, 예를들어 5,8 -> 5,9 의 경우를 생각해보자
주어진 문제에서 조건 중 "쿠션을 거쳐야하며 바로 목표값의 당구공을 칠 수 없다" 라고 나와있는데
이렇게 되면 상, 하 쿠션을 이용하는걸 생각해보자, 즉 5,8->5,9로 바로 치는게 아닌
5,8 -> 5,0 -> 5,9로 치는 상황이 있다.
따라서 해당 부분까지 처리해준다면 정답이 나온다.
'''
def solution(m, n, startX, startY, balls):
    answer = []

    for x2, y2 in balls:
        distances = []

        # 1. 위쪽 벽에 부딪혀서 돌아오는 경우
        distances.append((startX - x2) ** 2 + (startY - (-y2)) ** 2)  # 위쪽으로 반사
        # 2. 아래쪽 벽에 부딪혀서 돌아오는 경우
        distances.append((startX - x2) ** 2 + (startY - (2 * n - y2)) ** 2)  # 아래쪽으로 반사
        # 3. 왼쪽 벽에 부딪혀서 돌아오는 경우
        distances.append((startX - (-x2)) ** 2 + (startY - y2) ** 2)  # 왼쪽으로 반사
        # 4. 오른쪽 벽에 부딪혀서 돌아오는 경우
        distances.append((startX - (2 * m - x2)) ** 2 + (startY - y2) ** 2)  # 오른쪽으로 반사

        # 5. 공과 시작점이 같은 축에 있는 경우
        if startX == x2 and startY > y2:
            # X축이 같고 공이 아래쪽에 있을 때는 아래쪽 반사 경로 제거
            distances.remove((startX - x2) ** 2 + (startY - (-y2)) ** 2)
        elif startX == x2 and startY < y2:
            # X축이 같고 공이 위쪽에 있을 때는 위쪽 반사 경로 제거
            distances.remove((startX - x2) ** 2 + (startY - (2 * n - y2)) ** 2)

        if startY == y2 and startX > x2:
            # Y축이 같고 공이 왼쪽에 있을 때는 왼쪽 반사 경로 제거
            distances.remove((startX - (-x2)) ** 2 + (startY - y2) ** 2)
        elif startY == y2 and startX < x2:
            # Y축이 같고 공이 오른쪽에 있을 때는 오른쪽 반사 경로 제거
            distances.remove((startX - (2 * m - x2)) ** 2 + (startY - y2) ** 2)

        answer.append(min(distances))

    return answer

m=10
n=10
startX=3
startY=7
balls=[[7, 7], [2, 7], [7, 3]]

m=10
n=10
startX=5
startY=9
balls=[[5,8]]
print(solution(m,n,startX,startY,balls))