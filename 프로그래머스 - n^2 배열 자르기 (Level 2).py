'''내 풀이 틀린점 정리
1. n의 범위가 10^7 까지였는데 무지성 브루트포스로 생각하려다 10^14가 될뻔해서 빠른포기.
2. %,// 사용 후 +1 한다는거까진 좋았으나, if문을 잘못 걸어서 에러
3. tc 12,13이 runtime error 이 발생하길래, 검색해보니 left,right 를 int로 변환해줘야 함. 아마 음수 때문인듯?
'''
# def solution(n, left, right):
#     answer=[]
#     for i in range(left,right+1): #0~7
#         if i % n == n-1:
#             answer.append(i%n + 1)
#         else:
#             answer.append(i//n + 1)
#     return answer

def solution(n, left, right):
    answer=[]
    for i in range(int(left),int(right)+1): #0~7
        a = i%n
        b = i//n
        answer.append(max(a+1,b+1))
    return answer


n=3
left = 2
right = 5

n = 4
left = 7
right = 14
print(solution(n,left,right))