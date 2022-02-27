# from collections import deque
# case = int(input())
# graph = [list(map(int,input())) for _ in range(case)]
# count = 0
# ans = []
# def dfs(x,y):
#     global count
#     if x<0 or x>=case or y<0 or y>=case:
#         return False
#
#     if graph[x][y] == 1:
#         count+=1
#         graph[x][y]=0
#         dfs(x-1,y+0)
#         dfs(x+1,y+0)
#         dfs(x,y-1)
#         dfs(x,y+1)
#         return True
#
# for i in range(case):
#     for j in range(case):
#         if dfs(i,j)==True:
#             ans.append(count)
#             count=0
#
# print(len(ans),sep='\n')
# ans.sort()
# print(*ans, sep='\n')



from collections import deque
case = int(input())
graph = [list(map(int,input())) for _ in range(case)]
visited = [[False]*case for _ in range(case)]

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count=0
    q = deque()
    q.append((x,y))
    visited[x][y]=True

    while q:
        now = q.popleft()

        for i in range(4):
            nx = now[0]+dx[i]
            ny = now[1]+dy[i]
            if x < 0 or x >= case or y < 0 or y >= case:
                if graph[nx][ny]==1 and visited[nx][ny]==False:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    count+=1
    return count


ans=[]
total=0
for i in range(case):
    for j in range(case):
        if graph[i][j]==1:
            ans.append(bfs(i,j))
            total+=1

print(ans)
