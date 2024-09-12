def eratosthenes(n):
    temp=[True]*(n+1)
    arr=[i for i in range(n+1)]
    for i in range(2,int(n**0.5)+1):
        if arr[i] == 0:
            continue
        for j in range(i*i,n+1,i):
            arr[j]=0
            temp[j]=False
    return temp

def is_primeMultiple(x,eratos):

    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            q = x//i
            if eratos[i] and eratos[q]:
                return True
    return False


def solution(N,P,Q):
    eratos = eratosthenes(N)

    realans=[]
    for i,j in zip(P,Q):
        temp2=[x for x in range(i,j+1) if eratos[x]==False]
        ans = []
        for z in temp2:
            if is_primeMultiple(z,eratos):
                ans.append(z)
        realans.append(len(ans))
    return(realans)

N=26
P=[1,4,16]
Q=[26,10,20]
print(solution(N,P,Q))