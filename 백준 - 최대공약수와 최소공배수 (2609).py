a,b = map(int,input().split())

def gcd(a,b):
    for i in range(min(a,b), 0, -1):
        if a%i==0 and b%i==0:
            minimal = i
            break
    for i in range(max(a,b), (a*b)+1):
        if i%a == 0 and i%b == 0:
            maximal = i
            break
    return minimal,maximal

ans1,ans2 = gcd(a,b)
print(ans1)
print(ans2)


