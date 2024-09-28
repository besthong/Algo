from collections import deque
n,m = map(int,input().split())
temp = list(map(int,input().split()))
q = deque([i+1 for i in range(n)]) # [1 2 3 4 5 6 7 8 9 10]
cnt=0
for i in temp:
    point = q.index(i) #현재 찾고자하는 값의 위치
    left = point           #좌측에서 point까지의 거리
    right = len(q)-left       #total길이 - left = right 거리
    while True:
        if q[0]==i:
            q.popleft()
            break
        elif left<right or left==right:        #왼쪽이 비용이 적을경우 왼쪽으로 이동
            cnt+=1
            q.append(q.popleft()) # 맨 앞 값 맨뒤로 보냄

        elif left>right or left==right:        #오른쪽이 비용이 더 적을경우 오른쪽으로 이동
            cnt+=1
            q.appendleft(q.pop())
print(cnt)

