'''
문제를 요약해보자면 진법 변환 후 문제에 주어진 조건에 의하여 나눠진 수 중 소수를 찾는 문제이다.
convertTo 라는 진법변환 함수를 만들고, isPrime라는 소수판별 함수로 풀었다.
'''
def convertTo(n,k):
    T='0123456789ABCDEF'
    q,r = divmod(n,k)
    return convertTo(q,k)+T[r] if q else T[r]

def isPrime(n):
    n=int(n)
    if n==1:
        return False

    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    converted = str(convertTo(n,k)).split('0')
    print(converted)

    converted =[i for i in converted if i!='1' if i!='']
    print(converted)

    for i in converted:
        if isPrime(i):
            answer+=1

    return answer


n = 437674
k = 3
#
# n = 110011
# k=10

n=17
k=3

print(solution(n,k))