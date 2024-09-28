def solution(A):
    if len(A)==0:
        return 0

    min_price = A[0]
    max_price = 0

    for i in A:
        profit = i-min_price
        max_price=max(max_price,profit)
        min_price=min(min_price,i)

    return max_price

A=[23171,21011,21123,21366,21013,21367]
print(solution(A))