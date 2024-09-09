'''
5
6
8
10
12
100
'''

case = int(input())

def prime_nums(n):
    arr = [True] * (n+1)
    arr[0]=arr[1]=False

    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j]=False

    prime_num = [i for i,j in enumerate(arr) if j]
    return prime_num

prime_nums_list = prime_nums(1000000)
prime_num_set = set(prime_nums_list)

for i in range(case):
    num = int(input())
    count=0
    for i in prime_nums_list:
        if i > num//2:
            break
        if num - i in prime_num_set:
            count+=1

    print(count)
