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
