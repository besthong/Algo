def solution(name):
    answer = 0
    min_love = len(name) - 1

    while name[min_love] == 'A' and min_love > 0:
        min_love -=1

    if min_love<0:
        return answer

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) +1 )

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_love = min(min_love, i + (i + len(name)) - next)
    answer += min_love
    return answer

# def solution(name):
#     answer = 0
#
#     name = list(name)
#     a_list=0
#     dp=[0]*len(name)
#     for i in range(len(name)):
#         if name[i]=='A':
#             a_list+=1
#             dp[i]=a_list
#         else:
#             a_list = 0
#             dp[i]=a_list
#     print(dp)
#     print(dp.index(max(dp)))
#     start = dp.index(max(dp)) - dp[dp.index(max(dp))]
#     name1 = name[:start+1]
#     name2 = name[dp.index(max(dp))+1:]
#     name = name1+name2
#     print(name)
#
#     for i in name:
#         if i == 'A':
#             pass
#         else:
#             if abs((ord(i)-65)) < abs((ord(i)-90))+1: # A에서 이동하는 거리가 더 짧을경우
#                 answer+=abs(ord(i)-65)
#             elif abs((ord(i)-65)) > abs((ord(i)-90))+1: # Z에서 이동하는 거리가 더 짧을경우
#                 answer+=abs(ord(i)-90)+1
#             elif abs((ord(i)-65)) == abs((ord(i)-90))+1: # A에서 이동하나 Z에서 이동하나 같을경우
#                 answer+=abs(ord(i)-65)
#         answer+=1
#     if 'A' not in name:
#         answer-=1
#     return answer


name = "JAZ"
# name = "JAN"
# name = "JEROEN"
# name = "ABAAAAAAAAABB"
print(solution(name))