import sys
input = sys.stdin.readline

n = int(input())
b = int(input())

start,end = 1,n*n
ans=0
while start<=end:
    mid = (start+end) // 2
    total = 0
    for i in range(1,n+1):
        total+=min(mid//i, n)

    if total>=b:
        end = mid-1
        ans=mid
    else:
        start = mid+1
print(ans)
