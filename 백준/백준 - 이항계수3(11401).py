n,k = map(int,(input().split()))
p=1000000007
def power(a,b):
    if b==1:
        return a%p
    else:
        temp = power(a,b//2)
        if b%2==0:
            return (temp*temp)%p
        else:
            return (temp*temp*a)%p

fact = [1 for _ in range(n+1)]
for i in range(2,n+1):
    fact[i] = fact[i-1]*i%p

A=fact[n]
B=(fact[n-k] * fact[k])%p

print((A%p) * (power(B, p-2) % p)%p)