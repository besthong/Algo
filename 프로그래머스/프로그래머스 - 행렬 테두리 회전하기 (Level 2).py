def solution(rows,columns,queries):
    answer=[]
    rectangle=[[0]*columns for _ in range(rows)]
    count=1

    for i in range(rows):
        for j in range(columns):
            rectangle[i][j] += count
            count+=1

    for q in queries:
        q=list(map(lambda x:x-1 , q))
        temp = rectangle[q[0]][q[1]]
        minimal = temp

        for i in range(q[0]+1, q[2]+1):
            rectangle[i-1][q[1]] = rectangle[i][q[1]]
            minimal = min(minimal, rectangle[i][q[1]])

        for i in range(q[1]+1, q[3]+1):
            rectangle[q[2]][i-1] = rectangle[q[2]][i]
            minimal = min(minimal, rectangle[q[2]][i])

        for i in range(q[2]-1, q[0]-1 , -1):
            rectangle[i+1][q[3]] = rectangle[i][q[3]]
            minimal = min(minimal, rectangle[i][q[3]])

        for i in range(q[3]-1, q[1]-1, -1):
            rectangle[q[0]][i+1] = rectangle[q[0]][i]
            minimal = min(minimal, rectangle[q[0]][i])

        rectangle[q[0]][q[1]+1] = temp
        answer.append(minimal)

    return answer

rows=6; columns=6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
#
# rows = 3; columns = 3
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows,columns,queries))