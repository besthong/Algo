def solution(A):
    ls=[0]*len(A)
    rs=[0]*len(A)

    #왼->오 가면서 최대합 구하기/ 슬라이스가 적용되어야하므로 X+1 ~ Y-1 까지
    for i in range(1,len(A)-2):
        ls[i]=max(ls[i-1]+A[i],0)

    #오->왼 가면서 최대합 구하기 / 슬라이스가 적용되어야하므로 Y+1 ~ Z-1 까지
    for i in range(len(A)-2, 1, -1):
        rs[i]=max(rs[i+1]+A[i],0)

    # 처음 max값을 Y==1이라 가정하고 초기화
    max_=ls[0]+rs[2]

    #슬라이스때문에 1부터 len(A)-1까지로 정의하며, 각각 범위에서 최대값 계산
    for i in range(1,len(A)-1):
        max_ = max(max_,ls[i-1]+rs[i+1])
    return max_
A=[3,2,6,-1,4,5,-1,2]
print(solution(A))
