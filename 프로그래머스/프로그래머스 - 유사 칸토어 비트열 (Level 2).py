'''
1은 11011, 0은 00000으로 치환해서 풀면 되는 문제이다.
여기서 고려해야할점은 5**n까지 숫자가 늘어나므로 단순하게 replace하고, count를 하면 바로 시간초과가 발생한다.

숫자를 잘 보면 규칙이 존재한다 11011 -> 11011 11011 00000 11011 11011
이런식으로 11011을 기준으로 숫자가 늘어나는것을 볼 수 있다.
따라서 각 1 1 0 1 1 을 재귀함수로 반복하면서 풀었다.
'''

def solution(n, l, r):
    # n번째 유사 칸토어 비트열의 길이는 5^n
    def cantor_count(n, start, end, l, r):
        # base case: 0번째 유사 칸토어 비트열은 "1"이고 길이는 1
        if n == 0:
            return 1 if l <= start <= r else 0

        # 현재 n번째 비트열의 길이 (5^n)
        length = 5 ** n
        segment_length = length // 5  # 각 구간의 길이는 5등분

        # 구간별로 패턴이 11011로 반복됨
        count = 0
        for i in range(5):
            segment_start = start + i * segment_length
            segment_end = segment_start + segment_length - 1

            # 주어진 범위 (l, r)와 현재 구간의 범위 (segment_start, segment_end)이 겹치는지 확인
            if r < segment_start or l > segment_end:
                continue  # 현재 구간이 (l, r) 범위 밖이면 무시
            if i == 2:  # 가운데 구간은 00000, 즉 1의 개수가 0
                continue
            if i == 0 or i == 1 or i == 3 or i == 4:  # 11011의 1이 있는 부분
                count += cantor_count(n - 1, segment_start, segment_end, l, r)
        return count
    # 전체 비트열에서 구간 l~r까지의 1의 개수를 구함
    return cantor_count(n, 1, 5 ** n, l, r)

n=2
l=4;r=17
print(solution(n,l,r))