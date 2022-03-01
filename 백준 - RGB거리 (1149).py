case = int(input())
house = [list(map(int,input().split())) for _ in range(case)]
for i in range(1,case):
    for j in range(3):
        if j==0:
            house[i][j] = min(house[i][j]+house[i-1][j+1], house[i][j]+house[i-1][j+2])
        elif j==1:
            house[i][j] = min(house[i][j]+house[i-1][j-1], house[i][j]+house[i-1][j+1])
        else:
            house[i][j] = min(house[i][j]+house[i-1][j-2], house[i][j]+house[i-1][j-1])

print(min(house[-1]))

