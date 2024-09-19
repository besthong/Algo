'''
이번 문제는 데이터 두개를 추출하여 절대값인 최소값을 찾으면 된다.
우선 정렬을 하고 투포인터로, left,right를 설정한다음 최소값을 업데이트 하면 되는데
최소값이 음수일경우 left+=1, 아닐경우 right -= 1을 해주면서 반복하면 된다.
sort함수의 n*log(n) 과 투포인터의 n으로 시간복잡도 O(n*log(n))이다.
'''
def solution(A):
    A.sort()

    left=0
    right=len(A)-1

    min_=float('inf')

    while left<=right:
        cur_sum = A[left]+A[right]
        min_=min(min_,abs(cur_sum))

        if cur_sum<0:
            left+=1
        else:
            right-=1
    return min_

A=[-8,4,5,-10,3]
A=[1,4,-3]
A=[1]
print(solution(A))