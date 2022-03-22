'''
문자열의 길이가 5개밖에 없어서
product(중복순열) 로 모든 케이스를 구한 후 index 로 값을 찾았다.
'''


# from itertools import product
# def solution(word):
#     answer = 0
#     arr = []
#     for i in range(1,6):
#         arr += list(map(''.join, product("AEIOU",repeat=i)))
#
#     arr.sort()
#     answer = arr.index(word)+1
#
#     return answer


def solution(word):
    char = {'A':0, 'E': 1, 'I':2, 'O':3, 'U':4}
    answer = len(word)
    re=781
    for i in word:
        answer += re * char[i]
        re = (re-1)//5
    return answer
word = 'AAAAE'
print(solution(word))