n = int(input())
n_list = sorted(list(map(int,input().split())))

m = int(input())
m_list = list(map(int,input().split()))

ans = []

'''
# 이진탐색 - 재귀 구현
def binarySearch(arr,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2

    if arr[mid]==target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr,target,start,mid-1)
    else:
        return binarySearch(arr,target,mid+1,end)
'''
# 이진탐색 - 반복문 구현 O(logN)
def binarySearch(arr,target,start,end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(len(m_list)):
    temp = binarySearch(n_list,m_list[i],0,len(n_list)-1)
    if temp is None:
        ans.append(0)
    else:
        ans.append(1)
print(*ans,sep='\n')