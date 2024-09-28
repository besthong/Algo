from itertools import permutations

def isPrime(num):
    if num==1 or num==0:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def solution(numbers):
    ans = []
    for i in range(1,len(numbers)+1):
        tmp=list(permutations(numbers,i))
        for j in range(len(tmp)):
            num = int(''.join(map(str,tmp[j])))
            if isPrime(num):
                ans.append(num)
    ans=list(set(ans))
    return len(ans)
numbers='011'
print(solution(numbers))