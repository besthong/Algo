'''
Q.
A non-empty array A consisting of N integers is given.
A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].
For example, the following array A:
    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly three peaks: 3, 5, 10.
We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:
A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).
The goal is to find the maximum number of blocks into which the array A can be divided.

Array A can be divided into blocks as follows:
one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.

However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].
The maximum number of blocks that array A can be divided into is three.
Write a function:
def solution(A)
that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.
If A cannot be divided into some number of blocks, the function should return 0.
For example, given:
    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].

'''
peak=[3,5,10]


def isPossible(A,peaks,k):
    block_size = len(A)//k  # ex) peaks=[3,5,10] len(A)=12 -> 12/3=4 가 블록 사이즈
    block_found = [False]*k # False로 초기화시키며

    for peak in peaks:
        block = peak // block_size  # 3 // 4 이 코드를 통해 각 구역별로 peak가 존재하는지 알 수 있다. 예를들어 3//4 -> 0, 5//4 1 이런식
        block_found[block] = True #각 block구역을 True로 변환하여

    return all(block_found) # 모두 True일경우, all함수는 음수가 존재하거나 0이 존재할경우 False를 리턴한다.

def solution(A):
    peaks=[]

    for i in range(1,len(A)-1):
        if A[i-1]<A[i]>A[i+1]:
            peaks.append(i)
    k = len(peaks)  #최대로 구간을 나눌수있는 조건은 peaks의 개수만큼이 일단 최대이다.

    if len(peaks)==0: #peaks가 0인경우는 0으로 리턴
        return 0

    while k:
        if len(A)%k==0 and isPossible(A,peaks,k): # A를 정확히 K개 만큼 나눌 수 있어야하며, isPossbile가 True여야함 , 만약 len(A)=12, k=5일 경우 정확히 나눌수가없기때문에 k를 줄여야한다.
            return k
        else:
            k-=1
    return 0

A=[1,2,3,4,3,4,1,2,3,4,6,2]
A = [1, 3, 2, 1, 5, 4, 7, 6, 5, 4, 9, 8, 1]


print(solution(A))


