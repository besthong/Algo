'''
A non-empty array A consisting of N integers is given. The unique number is the number that occurs exactly once in array A.

For example, the following array A:

  A[0] = 4
  A[1] = 10
  A[2] = 5
  A[3] = 4
  A[4] = 2
  A[5] = 10
contains two unique numbers (5 and 2).

You should find the first unique number in A. In other words, find the unique number with the lowest position in A.

For above example, 5 is in second position (because A[2] = 5) and 2 is in fourth position (because A[4] = 2). So, the first unique number is 5.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the first unique number in A. The function should return −1 if there are no unique numbers in A.

For example, given:

  A[0] = 1
  A[1] = 4
  A[2] = 3
  A[3] = 3
  A[4] = 1
  A[5] = 2
the function should return 4. There are two unique numbers (4 and 2 occur exactly once). The first one is 4 in position 1 and the second one is 2 in position 5. The function should return 4 bacause it is unique number with the lowest position.

Given array A such that:

  A[0] = 6
  A[1] = 4
  A[2] = 4
  A[3] = 6
the function should return −1. There is no unique number in A (4 and 6 occur more than once).

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].
'''

'''
비교적 쉬운문제였다. 리스트의 중복을 제외하고, 중복아닌 값 중 제일 앞에있는애를 가져오면 됐다.
Counter 함수를 사용하여 dict형태로 변경하고 각 key값의 카운팅을 했을때, 1인 데이터만 남겼다.
그 이후 가장 앞에 [0]번째 데이터를 출력하면 된다.
참고로 이 문법은 파이썬 3.7이상부터 가능하다. 3.7이상부터 dict에도 순서를 보존하는 기능이 추가됐기 때문이다.
'''
from collections import Counter

def solution(A):
    counter = Counter(A)
    t = [key for key,value in counter.items() if value==1]
    if len(t)>0:
        return t[0]
    else:
        return -1
A=[4,10,5,4,2,10]
print(solution(A))