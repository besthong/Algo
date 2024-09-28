def solution(answers):
    ans = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,3,3,4,4,5,5]
    a_count,b_count,c_count=0,0,0
    for i in range(len(answers)):
        if a[i%5]==answers[i]:
            a_count+=1
        if b[i%8]==answers[i]:
            b_count+=1
        if c[i%10]==answers[i]:
            c_count+=1
    ans=[a_count,b_count,c_count]
    maxval = max(ans)
    realans=[]

    for i in range(len(ans)):
        if ans[i]==maxval:
            realans.append(i+1)

    return realans

answers=[1,2,3,4,5]
# answers=[1,3,2,4,2]
print(solution(answers))