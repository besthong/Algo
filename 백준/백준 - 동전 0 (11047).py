n,k = map(int,input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
coins = coins[::-1]
count=0
for i in coins:
    if k>=i:
        count+=k//i
        k-=i*(k//i)
print(count)