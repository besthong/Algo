def solution(n,computers):

    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == 0:
                dfs(j)

    ans=0
    visited = [0 for x in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            dfs(i)
            ans+=1
    return ans

n = 3
computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))