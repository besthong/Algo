case =int(input())
temp = list(map(int,input().split()))

def gcd(a,b):
    if b==0:
        return a
    else: return gcd(b,a%b)

for i in range(1,len(temp)):
    if temp[0]%temp[i]==0:
        a = temp[0]//temp[i]
        print(str(a)+"/"+"1")
    else:
        t =  gcd(temp[0],temp[i])
        print(str(temp[0]//t)+"/"+str(temp[i]//t))

