def solution(s):
    answer = ''
    s = list(s)

    count = 0
    for i in s:
        if i==' ':
            answer+=i
            count=0
        else:
            if count % 2 == 0:
                answer+=i.upper()
            else:
                answer+=i.lower()
            count+=1

    return answer
s = "try hello world"
print(solution(s))
