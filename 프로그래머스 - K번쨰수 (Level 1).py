def solution(array,commands):
    ans = []
    for i in commands:
        new = array[i[0]-1:i[1]]
        new.sort()
        ans.append(new[i[2]-1])

    return ans

array = [1,5,2,6,3,7,4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))