'''
4 3
11
13
16
18'''
import sys
input = sys.stdin.readline

n,c = map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])

start, end = 1, arr[-1]-arr[0]

ans = 0
# 1 2 4 8 9
while start<=end:
    mid = (start+end)//2
    total = 1
    pos = arr[0]
    for i in range(len(arr)):
        if arr[i]-pos>=mid: # 현재 위치에서 첫번쨰 거리까지가 기준거리보다 크거나 같을경우 +1
            total += 1
            pos = arr[i]

    if total >= c:
        start = mid + 1
        ans=mid
    else:
        end = mid - 1
print(ans)
