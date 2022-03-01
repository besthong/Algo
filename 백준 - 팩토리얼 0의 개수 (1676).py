case = int(input())
def dpFactorial(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans*i
    return ans

ans = list(str(dpFactorial(case)))[::-1]
for i in range(len(ans)):
    if ans[i]!='0':
        print(i)
        break
    elif i==len(ans):
        print(0)

