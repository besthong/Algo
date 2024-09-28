'''top down 방식'''
# def solution(t):
#     answer = 0
#
#     for i in range(1,len(t)):
#         for j in range(i+1):
#             if j==0:
#                 t[i][j] += t[i-1][j]
#             elif i==j:
#                 t[i][j] += t[i-1][j-1]
#             else:
#                 t[i][j] += max(t[i-1][j], t[i-1][j-1])
#
#     return max(max(t))

'''bottom up 방식'''
def solution(t):
    t = t[::-1]

    for i in range(len(t)-1): # 2번째부터 시작
        for j in range(len(t[i+1])):
            t[i+1][j] += max(t[i][j],t[i][j+1])
    return t[-1][0]

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))