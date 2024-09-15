'''
문제 자체는 쉬웠는데, 마지막 extreme large 데이터 케이스가 통과를 못해서 꽤 애먹었다.
요점은 결국 1과 2의 경우의수로 갈 수 있다면 피보나치를 사용할수있다.
이 때, 문제에서 원하는값은 결국 답을 2^B[i]로 나눠 나머지값을 가져오는 것이다.(mod 연산)
문제는 내가 처음 풀었던 코드로는 시간복잡도를 통과하지 못한다 O(L**2)

이유는 피보나치의 숫자는 생각보다 금방 커지는데, 큰 수에 대해 모듈러 연산을 진행하려면 비용이 커지기때문에 시간초과가 날 수 있다.
따라서 피보나치 수열을 계산하면서 동시에 모듈러 연산을 통해 숫자를 최대한 작게 만든다.

그 이후 비트연산자 O(1) 를 사용하여 1 << B[i]로 나누면 시간복잡도를 통과할수있다.
'''

#시간초과코드👇🏻
# def solution(A,B):
#     fibo=[1,2]
#     ans=[]
#
#     B=[1<<x for x in B]
#
#     while fibo[-1]<=max(A):
#         fibo.append(fibo[-1]+fibo[-2])
#     for a,b in zip(A,B):
#         sum = fibo[a-1]
#         ans.append(sum%b)
#     return ans

# def solution(A, B):
#     fibo=[0]*(max(A)+1)
#     fibo[0],fibo[1]=[1,2]
#
#     for i in range(2,max(A)):
#         fibo[i]=fibo[i-1]+fibo[i-2]
#
#     ans = []
#     for a, b in zip(A, B):
#         mod_value = 1 << b
#         ans.append(fibo[a - 1] % mod_value)
#     return ans

#정답코드👇🏻
def solution(A, B):
    L = len(A)
    max_rung = max(A)
    max_mod = max(B)

    # 2^B[i]를 미리 계산합니다.
    max_power = (1 << max_mod)  # 최대 2^B[i] 값을 구합니다.

    # 피보나치 수열을 2^B[i]의 최대값에 맞춰서 미리 계산합니다.
    fib = [0] * (max_rung + 2)
    fib[1] = 1
    for i in range(2, max_rung + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) % max_power

    result = []

    # 각 A[i]와 B[i]에 대해 답을 구합니다.
    for i in range(L):
        result.append(fib[A[i] + 1] % (1 << B[i]))

    return result


A=[4,4,5,8,1]
B=[3,2,4,3,1]
print(solution(A,B))