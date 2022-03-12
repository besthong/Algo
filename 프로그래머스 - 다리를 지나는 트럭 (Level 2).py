def solution(bridge_length, weight, truck_weights):
    suc = [] # 다리를 완전히 건넌 차량 리스트
    ing = [0]*bridge_length # 다리를 건너는 중인 차량 리스트
    size = truck_weights
    time = 0

    while len(suc) < size: #트럭이 모두 지나기 전까지
        time += 1
        top = ing.pop(0)

        if top != 0:
            suc.append(top)
        if len(truck_weights) > 0:
            if sum(ing) + truck_weights[0] <= weight:
                ing.append(truck_weights.pop(0))
            else:
                ing.append(0)
    return time
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]
print(solution(bridge_length, weight, truck_weights))