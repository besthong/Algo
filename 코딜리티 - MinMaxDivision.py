def solution(K,M,A): # K: 블록 개수, M: 배열에서 가장 큰 값, A: 입력배열
    right = sum(A)
    left = max(A)

    while left<=right:
        mid=(left+right)//2 # mid = (sumA+maxA)//2 #값은 최대 M부터 ~ sum(A)가 된다 따라서 각각을 left, right로 설정. 또한 그의 중간값인 mid부터 이진탐색 시작
        sum_t = 0
        block_cnt = 1

        for i in A:
            sum_t += i
            if sum_t > mid: #블록의 최대값이 mid를 넘는 순간
                sum_t = i # 블록의 최대값이 mid값을 넘었으므로, 새 블록 생성한다.
                block_cnt+=1

        if block_cnt<=K:
            right = mid-1
        else:
            left = mid + 1
    return left

K=3;M=5;A=[2,1,5,1,2,2,2]
print(solution(K,M,A))
