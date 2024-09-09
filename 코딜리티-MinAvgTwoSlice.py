# list = [-14, 7, 2, 10, -4, 9, -10]
# list=[4,2,2,5,1,5,8]
list= [1, 2, 3, 4, 100]

def solution(A):

    N = len(A)
    # 초기 값을 설정 (최소 평균을 구할 수 있는 배열의 크기는 2부터 시작)
    min_average = float('inf')
    min_index = 0

    # 길이가 2인 슬라이스를 확인
    for i in range(N - 1):
        avg = (A[i] + A[i + 1]) / 2
        print(avg)
        if avg < min_average:
            min_average = avg
            min_index = i
    print()
    # 길이가 3인 슬라이스를 확인
    for i in range(N - 2):
        avg = (A[i] + A[i + 1] + A[i + 2]) / 3
        print(avg)
        if avg < min_average:
            min_average = avg
            min_index = i

    return min_index
print(solution(list))
def solution(A):
    # Implement your solution here
    prefix=[0]*len(A)
    prefix2=[0]*len(A)

    prefix[0]=A[0]
    prefix2[0]=A[0]
    prefix2[1]=A[1]
    for i in range(1,len(A)):
        prefix[i]=(A[i]+A[i-1])/2

    for i in range(2,len(A)):
        prefix2[i]=(A[i]+A[i-1]+A[i-2])/3
    print(prefix[1:])
    print(prefix2[2:])
    ans=min(min(prefix[1:]),min(prefix2[2:]))
    return A.index(ans)

print(solution(list))

# ans=float("inf")
#
# prefix_sum = [0]*len(list)
# prefix_sum2 = [0]*len(list)
# prefix_sum[0]=list[0]
# prefix_sum2[0]=list[0]
# prefix_sum2[1]=list[1]
# for i in range(1,len(list)):
#     prefix_sum[i]=(list[i]+list[i-1])/2
# print(prefix_sum)
#
# for i in range(2,len(list)):
#     prefix_sum2[i]=(list[i]+list[i-1]+list[i-2])/3
# print(prefix_sum2)
#
# ans=min(min(prefix_sum2,prefix_sum))
# print(list.index(ans))


# prefix_sum = [0]*len(list)
# prefix_sum[0]=list[0]
#
# for i in range(1,len(list)):
#     prefix_sum[i]+=prefix_sum[i-1]+list[i]
#
# print(prefix_sum)
#
# ans=9999
# for i in range(len(prefix_sum)):
#     for j in range(1,len(prefix_sum)):
#         ans=min(ans,(prefix_sum[j]-prefix_sum[i])//(j-i)+1)
# print(ans)
