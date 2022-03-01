case = int(input())
nums = list(map(int,input().split()))
operand = list(map(int,input().split()))

maximum = -1e9
minimum = 1e9

def dfs(dept, total, plus, minus, multiply, divide):
    global maximum,minimum
    if dept == case:
        maximum = max(total,maximum)
        minimum = min(total,minimum)
        return

    if plus:
        dfs(dept+1, total+nums[dept] , plus-1, minus, multiply, divide)
    if minus:
        dfs(dept+1, total-nums[dept], plus, minus-1, multiply, divide)
    if multiply:
        dfs(dept+1, total*nums[dept], plus, minus, multiply-1, divide)
    if divide:
        dfs(dept+1, int(total/nums[dept]), plus, minus, multiply, divide-1)

dfs(1, nums[0], operand[0], operand[1], operand[2], operand[3])
print(maximum)
print(minimum)