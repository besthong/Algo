'''
Greedy 문제로 스택을 이용하여 어렵지 않게 구현가능
주의할점은 이미 내림차순일경우를 생각해보자.
'''
def solution(number,k):
    answer = ' '
    stack = [number[0]]

    for i in  number[1:]: # number 1번부터 시작해서
        while len(stack) > 0 and stack[-1] < i and k>0 : #스택 마지막값이 더 작을경우
            stack.pop()    # 스택에있는거 빼버림
            k-=1
        stack.append(i) #넘버에있는 맨앞에 값 스택에 넣기

    if k>0: #k값이 줄지 않았을경우, 즉 이미 내림차순 일 때
        stack=stack[:len(stack)-k]
    return "".join(stack)

number="654321"
k=5
print(solution(number,k))

#
#
# def solution(number, k):
#     answer=''
#     stack=[number[0]]
#
#     for num in number[1:]:
#         while len(stack)>0 and k>0 and stack[-1]<num:
#             stack.pop()
#             k-=1
#         stack.append(num)
#     if k>0:
#         stack=stack[:-k]
#     return "".join(stack)