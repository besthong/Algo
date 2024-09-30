'''
우선 우박수열부터 정리하자 -> collatz_sequence 어렵지 않게 구현 할 수 있다.
그 다음 각 범위를 고려해보면 사다리꼴 모양이 되는것을 알 수 있다.
예를들면 1,16 과 2,8의 범위를 구하고자 할때는, 이미 우박수열로부터 직선을 연결해두었으므로
정적분을 따져보면 사다리꼴 모양이 나온다.
이를 기반으로 모든 범위에 대한 합을 구하고
ranges 범위로 주어진 범위에 대해 마이너스로 해당 범위의 합만 구하면 된다.
'''

def collatz_sequence(k):
    seq = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3 * k + 1
        seq.append(k)
    return seq

def trapezoid_area(x1,y1,x2,y2):
    return (y1+y2)*(x2-x1)/2

def integral_of_collatz(k,integrals,seq):
    area=[0]*len(seq)
    for i in range(1,len(seq)):
        area[i]=area[i-1]+trapezoid_area(i-1,seq[i-1], i, seq[i])

    integrals[k]=area

def solution(k, ranges):
    answer = []
    integrals={}
    seq=collatz_sequence(k)
    integral_of_collatz(k,integrals,seq)
    print(integrals)

    for r in ranges:
        start,end = r
        end=len(seq) - 1 + end
        if start > end:
            answer.append(-1.0)
        else:
            answer.append(integrals[k][end]-integrals[k][start])

    return answer

k=5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]
print(solution(k,ranges))