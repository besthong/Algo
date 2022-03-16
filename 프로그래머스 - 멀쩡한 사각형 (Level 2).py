def gcd(a,b):
    if a>b: a,b=b,a
    while b:
        temp=a%b
        a=b
        b=temp
    return a

def solution(w,h):
    answer = 1
    return w*h-(w+h-gcd(w,h))


w=8;h=12
print(solution(w,h))