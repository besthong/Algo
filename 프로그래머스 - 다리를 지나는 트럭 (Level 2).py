def solution(bridge_length, weight, truck_weights):
    suc = [] # 다리를 완전히 건넌 차량 리스트
    ing = [0]*bridge_length # 다리를 건너는 중인 차량 리스트
    size = len(truck_weights)
    time = 0

    while len(suc) < size: #트럭이 모두 지나기 전까지
        time += 1
        top = ing.pop(0)    # 현재 다리에 있는 값 pop

        if top != 0:        # 다리에 차가 있었을경우 (2개짜리 list를 정의해둔상태)
            suc.append(top) # 성공적으로 건넘
        if len(truck_weights) > 0:
            if sum(ing) + truck_weights[0] <= weight: # 다리에 하나 더 올릴 수 있을때
                ing.append(truck_weights.pop(0)) # 하나 더 올림
            else:
                ing.append(0) # 다리 무게가 감당 못하면 하나만 넣고, 0 추가
    return time
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]
print(solution(bridge_length, weight, truck_weights))