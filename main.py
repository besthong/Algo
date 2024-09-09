def solution(a):
    answer = []

    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]

    one_cnt=0
    two_cnt=0
    three_cnt=0
    for i in range(0,len(a)):
        if one[i%5]==a[i]: one_cnt+=1
        if two[i%8]==a[i]: two_cnt+=1
        if three[i%10]==a[i]: three_cnt+=1

    temp=[one_cnt,two_cnt,three_cnt]
    big=max(temp)

    for i in range(len(temp)):
        if temp[i]==big:
            answer.append(i+1)
    return answer

a=[1,2,3,4,5]
print(solution(a))