
# def solution(logs):
#     answer = 0
#
#     for i in range(len(logs)):
#         if len(logs[i])>100:
#             answer+=1
#             continue
#         if 'team_name' in logs[i]:
#             logs[i] = logs[i].replace('team_name','')
#         if 'application_name' in logs[i]:
#             logs[i] = logs[i].replace('application_name','')
#         if 'error_level' in logs[i]:
#             logs[i] = logs[i].replace('error_level','')
#         if 'message' in logs[i]:
#             logs[i] = logs[i].replace('message','')
#         logs[i].replace(' ','')
#         temp=logs[i].split(':')
#         for i in range(len(temp)):
#             temp[i]=temp[i].lstrip().rstrip()
#         temp=temp[1:]
#
#         if len(temp)<4:
#             answer+=1
#             continue
#         for i in temp:
#             test=' '
#             if test in i:
#                 answer+=1
#                 break
#     return answer
#

# def solution(logs):
#     answer = -1
#     for i in logs:
#         temp=[]
#         temp = i.split(" ")
#         print(temp)
#         if 'team_name' not in temp or 'application_name' not in temp or 'error_level' not in temp or 'message' not in temp:
#             answer+=1
#             continue
#         elif len(temp)>100:
#             answer+=1
#             continue
#
#         for j in range(2,len(temp)+1,3):
#             print(j)
#
#             # if j%3==1:
#             #     if temp[j].isspace():
#             #         answer+=1
#             #         break
#     return answer
#
#
# #
#
#
# logs = ["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]
# print(solution(logs))
#
#
#
#























#
# def solution(orders):
#     answer = []
#     dic = {}
#     dic2 = {}
#     temp=[]
#     for i in orders: #리스트 분할
#         temp.append(i.split(' '))
#
#     for i in temp: #각 0번째 이름과 1번부터 음식들로 딕셔너리 만듦 dic
#         temp2=[]
#         temp2.append(i[1:])
#         if i[0] in dic:
#             dic[i[0]]+=(temp2)
#         else:
#             dic[i[0]] = temp2
#
#     for k,v in dic.items():  # dic 딕셔너리에서 value 리스트를 합친 후 중복제거, 새로운 dic2 생성
#         ans=[]
#         ans = sum(v,[])
#         final = list(set(ans))
#         dic2[k]=len(final)
#
#     realans=[]              #최종 답안 작성 리스트
#     max_=max(dic2.values()) #그중 가장 큰 값
#
#     for k,v in dic2.items(): #가장 큰값을 찾아서 list에 append작업
#         if v==max_:
#             realans.append(k)
#     realans.sort()
#     return realans
# orders=["alex pizza pasta", "alex pizza pizza", "alex noodle", "bob pasta", "bob noodle sandwich pasta", "bob steak noodle"]
# # orders=["alex pizza pasta steak", "bob noodle sandwich pasta", "choi pizza sandwich pizza", "alex pizza pasta steak"]
# # # answer = sorted(dic2.items(), key=lambda x:x[1],reverse=True)
# print(solution(orders))
# def solution(orders):
#     answer=[]
#     temp=[]
#     name = []
#     food = []
#     dic={}
#     for i in orders:
#         temp.append(i.split(" "))
#
#     for i in range(len(temp)):
#         if temp[i][0] not in name:
#             name.append(temp[i][0])
#
#     for i in temp:
#         food.append(i[1:])
#     print(temp)
#     print(name)
#     print(food)
#
#     for i in range(len(temp)):
#         if temp[i][0] in name:
#             dic[name
#     return answer

#
# def solution(accounts):
#     answer = 0
#
#     for i in accounts:
#         if i.isdigit():
#             if (i.startswith("010")and len(i)==11) or 12<=len(i)<=14:
#                 answer+=1
#     return answer
#
# accounts = ["01012345678","Th1s1sAccountNumber","9876543210123","2208875699"]
# # accounts = ["InvalidAccountNumber"]
# print(solution(accounts))
#
#
#
#
#
# def palindrome(num):
#     num = list(str(num))
#     first = ''.join(num)
#     after = ''.join(num[::-1])
#     if first==after:
#         return True
#     else:
#         return False
# def solution(n,m):
#     answer = 0
#     temp=[]
#     for i in range(n,m+1):
#         if palindrome(i):
#             temp.append(i)
#     return len(temp)
#
# n,m = 100,300
# print(solution(n,m))