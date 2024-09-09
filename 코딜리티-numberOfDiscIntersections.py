def solution(A):
    # 시작점과 끝점을 한 번에 계산하여 저장
    events = []
    for i in range(len(A)):
        events.append((i - A[i], 'start'))  # 시작점
        events.append((i + A[i], 'end'))    # 끝점

    # 이벤트를 정렬
    # 'start'는 앞에 오고, 'end'는 뒤에 오도록 정렬
    events.sort(key=lambda x: (x[0], x[1] == 'end'))
    print(events)

    cnt = 0
    active_discs = 0

    # 이벤트를 순회하며 교차하는 쌍 계산
    for event in events:
        if event[1] == 'start':  # 시작점인 경우
            cnt += active_discs
            active_discs += 1
        else:  # 끝점인 경우
            active_discs -= 1

        if cnt > 10000000:
            return -1

    return cnt