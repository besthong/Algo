'''
그놈의 소수찾기 문제 이지만
평소 제곱근으로 푸는 내 방식고 다르게
에라토스테네스의 체 알고리즘을 간단하게 푸는 방법이 있어서 가져와보고자 작성했다.
'''

'''아래는 내 제곱근 풀'''
def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = []
    for i in range(1, n+1):
        if isPrime(i):
            answer.append(i)
    return len(answer)

print(solution(10))



'''에라토스테네스의 체 이용'''
def solution(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))

    return len(num)

print(solution(10))