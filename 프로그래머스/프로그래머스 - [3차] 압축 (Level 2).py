'''
문제의 순서대로 따라가면 구현이 가능했지만
스택과 인덱스 슬라이싱 중 뭘 사용할까 고민하다가 쓸데없이 오래걸렸다.
결국 인덱스 슬라이싱을 사용해서 풀었던 풀이
'''

def solution(msg):
    answer = []
    word = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    start,end = 0,1
    while end<len(msg)+1:
        s = msg[start:end]      # K A K A O
        if s in word:
            end+=1
        else:
            answer.append(word.index(msg[start:end-1])+1)
            word.append(msg[start:end])
            start = end - 1
    answer.append(word.index(msg[start:end-1])+1)

    return answer

msg = 'KAKAO' # 11 1 27 15
msg = 'TOBEORNOTTOBEORTOBEORNOT'
msg = 'ABABABABABABABAB'
print(solution(msg))

#
# tmp = {chr(e+64): e for e in range(1,27)}
#
# print(tmp.items())