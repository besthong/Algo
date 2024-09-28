'''
문제를 분석해보니 홀,짝과 관련이 있었고,
//,% 연산자를 통해 값을 줄여나가며 나머지가 1일경우 즉 홀수일경우
battery+=1을 해주었다.

ps 다른사람의 풀이로는 bin(n)으로 1의 개수만 가져오는 방식도 있다.
'''
def solution(n):
    battery = 0
    while n!=1:
        #Return the tuple (x//y, x%y)
        b = n%2
        if b==1:
            battery+=1
        n = n//2
    battery+=1
    return battery

n=5000
print(solution(n))