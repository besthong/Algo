# num = 4
# pm = [1,3,5,7]

num = int(input())
pm = list(map(int,input().split()))

def isPrime(n):

    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

if 1 in pm:
    pm.remove(1)
result=0

for i in pm:
    prime = isPrime(i)
    if prime:
        result+=1

print(result)