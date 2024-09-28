from itertools import combinations
def solution(c):
    temp = []
    for i in range(len(c)+1):
        temp.append(list(combinations(c,i)))

    for i in range(2,len(temp)):
        for j in range(len(temp[i])):
            print(temp[i][j])

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)

#미완성