'''
그냥 조건 하나씩 따라하면 어렵지 않지만
반례가 생각보다 찾아내는게 힘들었다.
요점은 x#을 replace로 치환하는게 관건
'''

def replaceFunc(word):
    if '#' not in word:
        return word
    temp = []

    word=list(word)
    for i in range(len(word)):
        if word[i]!='#':
            temp.append(word[i])
        else:
            temp[-1]=temp[-1].lower()
    return "".join(temp)

def solution(m, musicinfos):
    answer = []
    m = replaceFunc(m)
    for i in musicinfos:
        i = list(i.split(","))
        i[3] = replaceFunc(i[3])
        hour = int(i[1].split(":")[0])-int(i[0].split(":")[0])
        minute = int(i[1].split(":")[1])-int(i[0].split(":")[1])
        totalTime = hour*60 + minute

        if totalTime>=len(i[3]):
            i[3]*=totalTime//len(i[3])
            i[3]+=i[3][:totalTime%len(i[3])]
        if totalTime<len(i[3]):
            i[3]=i[3][:totalTime]
        i.append(len(i[3]))

        answer.append(i)
    realans=[]
    for i in answer:
        if m in i[3]:
            i[0]=int(i[0].replace(":",""))
            realans.append(i)
    if len(realans)==0:
        return "(None)"
    realans = sorted(realans, key = lambda x:(x[4],-x[0]), reverse=True)
    return realans[0][2]


m = "ABCDEFG"
musicinfos = ["12:00,12:15,HELLO,CDEFGAB",
              "13:00,13:05,WORLD,ABCDEF"]


print(solution(m,musicinfos))