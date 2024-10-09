'''
비교적 쉬운문제였다, 그리디를 적용하면 풀 수 있는 문제이다.
A의 각 데이터보다, B를 크게 내면 되는 문제인데, A,B 모두 정렬 후 하나씩 비교하면서
만약 같거나, A가 더 클경우엔 j+=1만 해서 그 다음 B값이랑 비교하게 하면 되는 문제
'''
def solution(A, B):
    answer = 0
    A=sorted(A)
    B=sorted(B)
    j=0
    i=0
    while j<len(A):
        if A[i]<B[j]:
            answer+=1
            i+=1
            j+=1
        else:
            j+=1

    return answer

A=[5,1,3,7]
B=[2,2,6,8]

A=[1,3,9,9]
B=[2,2,8,10]
print(solution(A,B))