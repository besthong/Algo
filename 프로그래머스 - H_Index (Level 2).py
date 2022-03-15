'''
문제가 이해하기 어려웠다.
그래서 H-Index를 실제로 어떻게 구하나 구글링해보니
생각보다 간단했는데 아래와 같다.

나의 h는 어떻게 구할 수 있을까?
우측의 표와 같이 자신이 저널에 등재한 전체 논문중 많이 인용된 순으로 정렬한 후,
피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가 바로 나의 h가 됩니다.
'''
def solution(c):
    answer=0
    c.sort(reverse=True)
    # 0 1 3 5 6
    for i in range(len(c)):
        if c[i] <= i:
            answer = i
            return answer
        elif i==len(c)-1:
            return len(c)

# citations=[3,0,6,1,5]
citations=[10,10,10,10,10]
print(solution(citations))