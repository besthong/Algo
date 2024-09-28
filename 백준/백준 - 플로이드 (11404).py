# import sys
#
# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# inf=int(1e9)
#
# arr = [[inf]*n for _ in range(n)]
# for _ in range(m):
#     a,b,c = map(int, input().split())
#     arr[a-1][b-1] = min(arr[a-1][b-1],c)
#
# for k in range(n):
#     arr[k][k]=0
#     for i in range(n):
#         for j in range(n):
#             arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
#
# #
# # for i in arr:
# #     temp=' '.join(map(str,i))
# #     print(temp)
#
# for row in arr:
#     for i in range(n):
#         if row[i]==inf:
#             row[i]=0
#         print(row[i],end=" ")
#     print()


import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[float('inf')]*n for _ in range(n)]
print(*arr, sep='\n')


for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1],c)


for k in range(n):
    arr[k][k] = 0
    for i in range(n):
        for j in range(n):
            arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])

print(*arr, sep='\n')