'''
문제를 잘 읽어보고 생각해보면, 진입시 카메라 설치는 낭비가 되고,
카메라 설치는 진출시에 해야 최소개수로 가능하다.
따라서 해야 할 순서는
1. 진출이 가장 빠른 순서로 sort하기
2. 맨처음 진출한 부분에 카메라 설치
3. 반복하면서 카메라 설치하는데, 카메라가 설치된곳보다 진입을 먼저 한 곳이 있다면 그부분은 pass (겹치기때문에)
4. 그게 아닐경우에 카메라 += 1 후, 현재 카메라 위치를 cur_pos에 담아줌
'''
def solution(routes):
    answer = 1
    routes = sorted(routes, key = lambda x:x[1])
    print(routes)
    cur_pos = routes[0][1] # -15
    routes.pop(0)

    for i in routes:
        if i[0] < cur_pos:
            continue
        if i[0] > cur_pos:
            answer+=1
            cur_pos = i[1]

    return answer


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))