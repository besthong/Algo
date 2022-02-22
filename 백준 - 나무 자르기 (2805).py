'''
해당 문제는 parametric serach 로 풀 수 있다.
백준 사이트에서 시간초과가 뜨길래 구글링 해보니,
어떤 동작을 함수에 넣느냐 안넣느냐에 따라 속도 차이가 난다고 한다.
+ input 을 sys 모듈로 바꿔서 제출하니 통과함.
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int,input().split()))

def binarySearch():
    start, end = 1, max(arr)
    ans = 0
    while start<=end:
        mid = (start+end)//2
        total = 0

        for i in arr:
            if i-mid > 0:
                total += i-mid
            else:
                continue

        if total>=m:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    print(ans)

binarySearch()