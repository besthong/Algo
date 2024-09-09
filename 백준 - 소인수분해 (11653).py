# n = 72
n = int(input())
d = 2
if n==1:
    quit()
factorization=[]
while d<=n:
    if n%d==0:
        factorization.append(d)
        n/=d
    else:
        d+=1

for i in factorization:
    print(i)