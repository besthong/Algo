'''
소수값이 정수인지 판별하는 알고리즘을 잘못 작성해서
꽤나 고생했따 하하..

'''
def meet(a,b,e,c,d,f):
    if a*d==b*c:
        return None
    # x = round(((b*f)-(e*d))/((a*d)-(b*c)),1)
    # y = round(((e*c)-(a*f))/((a*d)-(b*c)),1)
    # if str(x).split('.')[1]=='0' and str(y).split('.')[1]=='0':
    #     return [int(x),int(y)]

    x = (b*f-e*d)/(a*d-b*c)
    y = (e*c-a*f)/(a*d-b*c)
    if x == int(x) and y == int(y):
        return [int(x),int(y)]



def solution(line):
    answer = []
    temp=[]

    for i in range(len(line)):
        for j in range(i+1,len(line)):
            a,b,e = line[i][0], line[i][1], line[i][2]
            c,d,f = line[j][0], line[j][1], line[j][2]
            temp.append(meet(a,b,e,c,d,f))
    temp = list(filter(None,temp))


    mergeX = [x[0] for x in temp]
    mergeY = [x[1] for x in temp]
    maxX,minX,maxY,minY = max(mergeX),min(mergeX),max(mergeY),min(mergeY)
    # res = [['.' for _ in range(maxX-minX+1)] for _ in range(maxY-minY+1)]
    res = ['.' * (maxX-minX+1)] * (maxY-minY+1)
    for x,y in temp:
        # res[maxY-y][x-minX] ='*'
        res[maxY-y] = res[maxY-y][:x-minX] + '*' + res[maxY-y][x-minX+1:]
    return [''.join(t) for t in res]

line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
print(solution(line))