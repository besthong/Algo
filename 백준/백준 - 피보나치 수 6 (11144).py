'''
input -> 1000 , output -> 517691607
피보나치 수 알고리즘중 행렬을 이용하는 방식
맨처음 내 풀이는 dp를 사용해서 시간복잡도를 줄이려고 했으나,
input 범위가 1,000,000,000,000,000,000 이므로, dp를 사용하면 공간복잡도가 초과됨,
따라서 행렬을 사용하는 방식으로 변경. 행렬 [1,1],[1,0] 의 제곱근을 구하다보면 피보나치수 형식이랑 같음
제곱근 구하는 방식은 O(logN)으로 구할 수 있는 recursion을 이용했다.
'''
n=int(input())
c=1000000007

def multiply(m1,m2):
    dummy=[[0]*2 for _ in range(2)]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1)):
                dummy[i][j] += m1[i][k]*m2[k][j]
            dummy[i][j]%=c
    return dummy

def power(a,b):
    if b==1:
        return a
    else:
        temp=power(a,b//2)
        if b%2!=0:
            return multiply(multiply(temp,temp),a)
        else:
            return multiply(temp,temp)

m=[[1,1],[1,0]]
print(power(m,n)[1][0])