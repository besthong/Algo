'''
다른사람풀이 1위 
왜 replace를 생각하지 못했을까

'''
def solution(s):
    dic={"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
     "eight": "8", "nine": "9"}

    for key, value in dic.items():
        s = s.replace(key,value)
    return int(s)

'''
생각이 짧았던 내 풀이.. ㅎㅎ
'''
# def solution(s):
#     answer = []
#     dic={'zero':0,
#          'one':1,
#          'two':2,
#          'three':3,
#          'four':4,
#          'five':5,
#          'six':6,
#          'seven':7,
#          'eight':8,
#          'nine':9}
#
#     temp=''
#     s = list(s)
#
#     while len(s)!=0:
#         if s[0].isdigit(): #숫자일경우 그냥 append
#             answer.append(s.pop(0))
#         elif s[0].isalpha(): #문자일경우
#             temp+=s.pop(0)
#             if temp in dic.keys():
#                 answer.append(dic[temp])
#                 temp=''
#     answer = ''.join(list(map(str,answer)))
#     return int(answer)


s="one4seveneight"
s = "23four5six7"
s="2three45sixseven"
s="123"
print(solution(s))