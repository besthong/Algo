n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]


start,end = 1,max(arr)
ans=0
while start<=end:
    mid = (start+end)//2
    total = 0
    for i in arr:
        total += i // mid

    if total>=k:
        start = mid + 1
        ans=mid
    else:
        end = mid -1

print(ans)
