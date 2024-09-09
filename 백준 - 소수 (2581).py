n=int(input())
m=int(input())
# n=60;m=100

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

prime=[]
for i in range(n,m+1):
    if isPrime(i):
        prime.append(i)

if 1 in prime:
    prime.remove(1)
if len(prime) != 0:
    print(sum(prime))
    print(min(prime))
else:
    print(int(-1))
