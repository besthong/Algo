def solution(sizes):
    answer = 0
    biggest = 0
    smallest = 0
    for i in sizes:
        if i[0]<i[1]:
            i[0],i[1] = i[1],i[0]
        if i[0]>biggest:
            biggest=i[0]
        if i[1]>smallest:
            smallest=i[1]

    return biggest*smallest

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))