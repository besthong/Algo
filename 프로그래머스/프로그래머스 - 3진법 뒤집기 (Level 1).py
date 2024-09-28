'''
반복문 이용하여 3진법 변환 후
int 함수 사용해서 10진법으로 변환
'''
def solution(n):
    temp=[]
    while n>0:
        a=n%3
        temp.append(a)
        n=n//3
    temp = ''.join(map(str,temp))
    return int(temp,3)

n=45
n=125
print(solution(n))