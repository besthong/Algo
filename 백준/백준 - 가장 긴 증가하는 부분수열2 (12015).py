'''
LIS 알고리즘을 가장 쉽게 풀 수 있는 방법은 O(N^2)인 DP이지만
해당 문제에서는 O(nlogn) 으로 풀 수 있는 이진트리를 사용한다.
'''
case = int(input())
temp = list(map(int,input().split()))
dp=[temp[0]]

def binarySearch(target):
    start=0
    end=len(dp)-1

    while start<=end:
        mid = (start+end)//2

        if dp[mid] == target:
            return mid
        elif dp[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in temp:
    if dp[-1]<i:
        dp.append(i)
    else:
        index = binarySearch(i)
        dp[index] = i
print(len(dp))
