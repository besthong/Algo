'''이 코드로는 시간초과 발생함 이유는 각 P,Q의 영역의 소수가 아닌 수에 대해서 전부 소수의곱으로 이루어져있는지 확인하기때문'''
# def eratosthenes(n):
#     temp=[True]*(n+1)
#     temp[0]=temp[1]=False
#
#     arr=[i for i in range(n+1)]
#     for i in range(2,int(n**0.5)+1):
#         if arr[i] == 0:
#             continue
#         for j in range(i*i,n+1,i):
#             arr[j]=0
#             temp[j]=False
#     return temp
#
# def is_primeMultiple(x,eratos):
#
#     for i in range(1,int(x**0.5)+1):
#         if x%i==0:
#             q = x//i
#             if eratos[i] and eratos[q]:
#                 return True
#     return False
#
# def solution(N,P,Q):
#     eratos = eratosthenes(N)
#     realans=[]
#
#     for i,j in zip(P,Q):
#         temp2=[x for x in range(i,j+1) if eratos[x]==False]
#         ans = []
#         for z in temp2:
#             if is_primeMultiple(z,eratos):
#                 ans.append(z)
#         realans.append(len(ans))
#     return(realans)

# -------------------------------------------------------
'''
이 코드로는 통과 가능한데, 이유는 위에 코드에서는 소수를 검증하고, 각 정수가 소수로 이루어져있는지를 확인하는 과정이 있었으나,
아래 코드로는 반소수를 미리 계산 후, 누적합을사용하여 최대 N(ex 26) 즉 1~26까지의 정수에 대해 소수가 아닌 정수 중 소수의 곱으로 이루어진 데이터를 생성함
따라서 마지막엔 prime_sum[Q]-preim_sum[i-1]을 해주면, 각 범위의 반소수 개수의 합을 구할 수 있음.
O(N * log(log(N)) + M)
'''

def eratosthenes(n):
    is_prime=[True]*(n+1)
    is_prime[0]=is_prime[1]=False

    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j]=False
    return is_prime

def solution(N,P,Q):
    is_prime=eratosthenes(N)

    semiprime=[0]*(N+1)

    #반소수 여부 미리 계산
    for i in range(2,N+1):
        if is_prime[i]:
            for j in range(i,N//i+1):
                if is_prime[j]:
                    semiprime[i*j]=1

    #누적합으로 계산
    prime_sum=[0]*(N+1)
    for i in range(1,N+1):
        prime_sum[i]=semiprime[i]+prime_sum[i-1]

    #누적합 이용하여 결과리스트 생성
    realans=[]
    for i,j in zip(P,Q):
        realans.append(prime_sum[j]-prime_sum[i-1])
    return realans


N=26
P=[1,4,16]
Q=[26,10,20]
print(solution(N,P,Q))