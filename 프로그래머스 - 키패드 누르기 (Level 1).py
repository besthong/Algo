'''
맨처음 스택으로 할까 해서 구현하다가 보니
현재값을 저장하고 가져오는데에 불편함이 있어서 이중리스트로 구현했다.
리스트에 실제 1,2,3 값을 넣을 필요 없이 i,j 위치만 가지고 거리를 계산 하기 위해
arr을 만들었다.
노가다문제였따

'''
def solution(numbers, hand):
    answer = ''

    # 1 2 3 4 5 6 7 8 9 * 0 #
    arr = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2]]

    left=[3,0]
    right = [3,2]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer+='L'
            left = arr[i-1]
        if i== 3 or i == 6 or i == 9:
            answer+='R'
            right = arr[i-1]
        elif i == 2 or i == 5 or i == 8 or i == 0:
            if i==0: i = 11
            left_distance = abs(arr[i-1][0]-left[0])+abs(arr[i-1][1]-left[1])
            right_distance = abs(arr[i-1][0]-right[0])+abs(arr[i-1][1]-right[1])
            if left_distance == right_distance:
                answer+=hand[0].upper()
                if hand[0] == 'r': right = arr[i-1]
                else: left = arr[i-1]
            if left_distance < right_distance:
                answer+='L'
                left = arr[i - 1]
            if left_distance > right_distance:
                answer+='R'
                right = arr[i - 1]
    return answer

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = 'right'

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
print(solution(numbers,hand))
