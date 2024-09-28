'''
각 head, number, tail 을 나누는게 관건인거같다.
정규식으로 해결
'''
import re

def splited_string(file):
    head = re.match('[\D]+',file)  #정규식 match = 반드시 첫 문자열부터 시작한다. +는 앞문자가 1번 혹은 그 이상 반복되는 패턴
    number = re.search('[\d]+', file) #정규식 search = match와는 다르게 문자열 어디에나 위치해도 가능하다.
    ans = [head.group(), int(number[0]), file[number.end():]]
    return ans

def solution(files):

    answer=[]
    for i, file in enumerate(files):
        s = splited_string(file.lower())
        s.append(i)
        answer.append(s)

    answer = sorted(answer, key = lambda x:(x[0],x[1],x[-1]))
    realans = list(map(lambda x:files[x[-1]],answer))
    return realans


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

files = ["F-5 Freedom Fighter",
         "B-50 Superfortress",
         "A-10 Thunderbolt II",
         "F-14 Tomcat"]

print(solution(files))