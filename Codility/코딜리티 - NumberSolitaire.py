'''
6개의 숫자로 이루어진 주사위를 굴려 리스트 A에서 각 요소별 가장 큰 값을 찾는 문제
dp[i]는 A[i]+max(dp[i-1],dp[i-2],,,dp[i-6])로 구할 수 있다는게 키포인트이며,
만약 배열 자체의 크기가 6이하일경우는, 각 크기에 맞게 최대 합을 계산하면 된다.
'''

def solution(A):
    dp=[0]*len(A)
    dp[0]=A[0]
    for i in range(1,len(A)):
        dp[i]=max(dp[j] for j in range(max(0,i-6),i))+A[i]

    return dp[-1]

A=[1,-2,0,9,-1,-2]
print(solution(A))