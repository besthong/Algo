'''
맨 처음엔 도착지점 좌표만 넣고 set 했는데
다른방향에서 같은 지점으로 도착할때도 중복으로 판단해서 지워버리길래
가는 길을 아예 좌표로 넣고 범위에 맞게 if문 추가 후 set 하여 통과했
'''
def solution(dirs):
    answer = 0
    start=[0,0]
    test = []
    for i in list(dirs):
        if i == 'U' and start[1]<5: #위
            test.append((start[0],start[1]+0.5))
            start[1]+=1
        if i == 'D'and start[1]> -5: #아래
            test.append((start[0],start[1] - 0.5))
            start[1] -= 1
        if i == 'L' and start[0]> -5: #왼쪽
            test.append((start[0]-0.5,start[1]))
            start[0] -= 1
        if i == 'R' and start[0] < 5:
            test.append((start[0]+0.5,start[1]))
            start[0] += 1


    print(test)
    test = set(test)
    # print(test)
    # print(len(test))

    return len(test)


# dirs = "ULURRDLLU"
# dirs = "LULLLLLLU"
dirs = 'LRLRL'
print(solution(dirs))