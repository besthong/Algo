def solution(p,s):
    answer = []
    cnt=0
    while len(p)!=0:
        if p[0]<100:       # 맨 앞 작업이 100이 아닐경우
            p = [x+y for x,y in zip(p,s)]
        elif p[0]>=100:
            cnt+=1
            p=p[1:]
            s=s[1:]

            while len(p)!=0:
                if p[0]>=100:
                    cnt+=1
                    p=p[1:]
                    s=s[1:]
                else:
                    break
            answer.append(cnt)
        cnt=0

    return answer
# progress = [93,30,55]
# speed = [1,30,5]

progress=[95,90,99,99,80,99]
speed=[1,1,1,1,1,1]


realans=[]
realans=solution(progress,speed)
print(realans)