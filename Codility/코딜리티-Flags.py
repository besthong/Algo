def isPeak(peak,target):
    #첫번째 깃발부터 선택
    used_flag = 1
    last_flag = peak[0]

    for i in range(1,len(peak)):
        #현재 peak - last_flga 가 target보다 커야만
        if peak[i]-last_flag >= target:
            used_flag+=1
            last_flag = peak[i] #flag위치를 최신 상태로 수정함.
            if used_flag >= target: #현재 used_flag가 target과 ge일때 True로
                return True
    return False

def solution(A):
    peak=[]

    for i in range(1,len(A)-1):
        if A[i]>A[i-1] and A[i]>A[i+1]:
            peak.append(i)
    if len(peak)==1:
        return 1

    #binary search
    start=1
    end=len(peak)
    result=0
    while start<=end:
        mid = (start+end)//2
        if isPeak(peak,mid):
            result = mid
            start = mid+1
        else:
            end = mid-1
    return result
A=[1,5,3,4,3,4,1,2,3,4,6,2]
# A=[1,3,2]
A=[0, 0, 0, 0, 0, 1, 0, 1, 0, 1]
# A=[3,2,1]
print(solution(A))