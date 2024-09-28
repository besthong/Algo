'''
A[p]+A[q]>A[r] and A[q]+A[r]>A[p] and A[p]+A[r]>A[q]의 조건을 동시에 만족해야하는데
정렬 후 검증하게된다면, p<q<r을 항상 만족하기때문에 A[p]+A[q]>A[r]만 검증하면된다.
n이 최대 1000이므로, n**2까지는 괜찮다고 판단하였고, p+q를 투포인터로 두고, r을 while문으로 이동하면서 검증하도록 하였다.
여기 코드에서 반복문이 3중으로 보일 수 있으나, while문은 n만큼 반복되진 않기때문에 n**2로 나온다.
'''
def solution(A):
    if len(A)<3: return 0
    cnt=0
    A.sort()
    for p in range(len(A)-2):
        r = p+2
        for q in range(p+1,len(A)-1):
            while r<len(A) and A[p]+A[q]>A[r]:
                r+=1
            cnt+=r-q-1
    return cnt
A=[10,2,5,1,8,12]
print(solution(A))