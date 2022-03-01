'''
딕셔너리 O(1) 을 사용하여 풀어봤다.
'''
n = int(input())
n_list = sorted(list(map(int,input().split())))
m = int(input())
m_list = list(map(int,input().split()))


# 딕셔너리 사용
n_dic = {}
val=[]
count = 1
for i in n_list:
    if i in n_dic.keys():
        count+=1
    else:
        count=1
    n_dic[i] = count

for i in m_list:
    if i in n_dic.keys():
        val.append(n_dic[i])
    else:
        val.append(0)
print(*val)


# print(n_list)
# val=[]
#
# def binarySearch(arr,target,start,end):
#     ans=0
#     while start<=end:
#         mid = (start+end)//2
#
#         if arr[mid]==target:
#             ans+=1
#             arr.pop(mid)
#
#         elif arr[mid] > target:
#             end = mid-1
#         else:
#             start = mid+1
#     return ans
#
# for i in range(len(m_list)):
#     val.append(binarySearch(n_list,m_list[i],0,len(m_list)-1))
#
#
# print(val)