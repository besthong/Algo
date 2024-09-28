# from collections import Counter
# def divisible(n): #약수 구하기 알고리즘
#     temp=[]
#     for i in range(1,int(n**0.5)+1):
#         if n%i==0:
#             temp.append(i)
#             if n//i != i:
#                 temp.append(n//i)
#     return sorted(temp)
#
# def CountDivisible(temp,cntA): #각 숫자별 약수가 몇번 등장했는지 카운팅
#     ans=0
#     for i in temp:
#         ans+=cntA[i]
#     return ans
#
# def solution(A):
#     setA=list(set(A))
#     cntA = Counter(A) #Counter({3: 2, 1: 1, 2: 1, 6: 1})
#     dic={}
#     ans_dic={}
#
#     for i in setA:
#         dic[i]=divisible(i)
#
#     for i,j in dic.items():
#         ans_dic[i]=CountDivisible(j,cntA)
#
#     for i in range(len(A)): #전체 배열 A에서 각 숫자별 약수의 개수를 빼주면 약수가 아닌 갯수가 나온다
#         A[i]=len(A)-ans_dic[A[i]]
#     return A

#위 코드로는 시간복잡도가 n*log(n) 이지만 틀렸다고나온다.
#이유는 각 반복마다 약수를 직접 구하기때문인거같다. 따라서 직접 약수를 구하지말고 아래 코드처럼 미리 배열로 정의한다음 참조하는식으로 변경하면 통과한다.

def solution(A):
    N = len(A)
    num_non_divisors = [0] * N
    if N < 2:
        return num_non_divisors

    # 최대값과 발생 횟수 카운트
    MaxVal = max(A)
    Occur = [0] * (MaxVal + 1)

    for e in A:
        Occur[e] += 1

    # 약수 계산
    Divisors = [0] * (MaxVal + 1)
    for i in range(1, MaxVal + 1):
        k = i
        while k <= MaxVal:
            Divisors[k] += Occur[i]
            k += i

    # 각 숫자의 약수가 아닌 개수 계산
    for i in range(N):
        num_non_divisors[i] = N - Divisors[A[i]]

    return num_non_divisors


A = [3, 1, 2, 3, 6]
print(solution(A))

A=[3,1,2,3,6]
print(solution(A))