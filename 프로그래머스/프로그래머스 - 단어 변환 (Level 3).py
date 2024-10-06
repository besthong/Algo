'''
이번 문제는 너비우선탐색(BFS)로 풀었다.
begin의 단어가 target의 단어가 될 때 까지 words에 있는 단어들로만 변환하면서 추적하면 되는데
각 단어가 한개씩 변경이 가능하고 & 그게 words 리스트에 있다면 step을 증가시키는 방식으로 했다.
물론 visited를 따로 만들어 기존에 변환할때 사용된 words는 재사용하지않도록 했다.
'''

from collections import deque

def can_convert(word1,word2):
    dif_cnt=0
    for i,j in zip(word1,word2):
        if i!=j:
            dif_cnt+=1
        if dif_cnt>1:
            return False
    return True

def solution(begin, target, words):
    answer = 0

    queue=deque([(begin,0)])
    visited=[False]*len(words)

    while queue:
        cur_word,step = queue.popleft() #현재 큐,스텝

        if cur_word==target: #만약 단어가 완성됐다면, step 카운트를 반환
            return step

        for i in range(len(words)):
            if not visited[i] and can_convert(cur_word,words[i]):
                visited[i]=True
                queue.append((words[i],step+1))
    return 0


begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]
words=["hot", "dot", "dog", "lot", "log"]
print(solution(begin,target,words))