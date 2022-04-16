'''
이문제는 두가지를 구현하면 된다.
1. 진수변환 알고리즘
2. 인원수와 자기순번에 맞게 값을 빼오기

1번은 이번에 새로운 방법을 알게되어 적용해봤다.
예로, 16진수일경우 17부터는 10을 작성해야하는데 첫번째 a//b == 1 과 나머지 0을 더해주면 된다.

2번은 while문 하나로 O(n)으로 해결하고자 하였으나 도저히 생각이 안나서
이중반복문을 사용하여 최대 가져올 수 있는 list를 미리 작성 후 순번에 맞게 꺼내어오는 방식을 선택했다.

'''
def convertTo(n,base):
    T='0123456789ABCDEF'
    q, r = divmod(n,base)

    return convertTo(q,base)+T[r] if q else T[r]

def solution(n, t, m, p):
    answer = []

    i=0
    temp = []
    while len(temp)<=t*m:
        z = list(convertTo(i,n))
        i+=1
        for v in z:
            temp.append(v)

    while len(answer)!=t:
        if len(answer)==0:
            answer.append(temp[p-1])
        elif len(answer)!=0:
            p+=m
            answer.append(temp[p-1])
    return ''.join(answer)



n=2 # 진수
t=4  # 미리 구할 숫자 개수
m=2  # 게임에 참가하는 인원
p=1  # 내 순서
#result = 0111
n=16;t=16;m=2;p=1

print(solution(n,t,m,p))