def solution(price, money, count):
    num=0
    for i in range(1,count+1):
        num+=price*i
    if money>num:
        return 0

    return num-money


price = 3
money = 20
count = 4

print(solution(price,money,count))
