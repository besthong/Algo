case = int(input())
room = []
for i in range(case):
    room.append(list(map(int,input().split())))
room = sorted(room, key = lambda x:(x[1],x[0]))
temp = [room[0][1]]
for i in range(len(room)-1):
    if temp[-1]<=room[i+1][0]:
        temp.append(room[i+1][1])

print(len(temp))