'''
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.
'''

#단순히 abs()를 사용하여 양의 정수로 변경 한 후, set하여 중복제거한다음 개수 리턴
#abs도 O(1), set도 O(1)이지만, 리스트반복이 있어 O(n)으로 끝낼 수 있다.
def solution(A):
    A=list(set(A))
    A=[abs(i) for i in A]
    A=set(A)
    return len(A)

A=[-5,-3,-1,0,3,6]
print(solution(A))