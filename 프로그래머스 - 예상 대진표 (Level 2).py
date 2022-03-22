import math

'''신기한 풀이'''
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()

'''시간초과 안나는 풀이'''
# def solution(n,a,b):
#     answer = 0
#     while True:
#         answer += 1
#         a = math.ceil(a/2)
#         b = math.ceil(b/2)
#         if a == b or a == 0 or b == 0:
#             break
#     return answer


'''내 시간초과 풀이'''
# def solution(n,a,b):
#     answer = 1
#     if a>b:
#         a,b=b,a
#     if (a == 1 and b == 2) or (a == 2 and b == 1):
#         return answer
#     while True:
#         a=math.ceil(a/2)
#         b=math.ceil(b/2)
#         answer+=1
#
#         if a%2!=0 and b==a+1:
#             break
#         elif a%2==0 and b==a-1:
#             break
#     return answer



n=16
a=9
b=12

print(solution(n,a,b))