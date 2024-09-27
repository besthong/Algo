'''
Write a function:

def solution(S)
that, given a string S, returns the index (counting from 0) of a character such that the part of the string to the left of that character is a reversal of the part of the string to its right. The function should return −1 if no such index exists.
Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.
For example, given a string:
"racecar"

the function should return 3, because the substring to the left of the character "e" at index 3 is "rac", and the one to the right is "car".
Given a string:
"x"

the function should return 0, because both substrings are empty.
Write an efficient algorithm for the following assumptions:
the length of string S is within the range [0..2,000,000].
'''

'''
문자열이 대칭 될 때 기준이 되는 문자의 index를 반환하면되는 문제이다.
데이터 개수가 최대 20만이라 N^2으로 풀면 시간초과가 발생한다 
따라서 O(n)에 끝내고자 투포인터로 풀어봤다. 
-1을 반환하는 조건값을 헷갈려서 틀렸었는데, 일단 짝수인경우 "abba" 는 완벽한 대칭이 이뤄지므로 특정 문자를 기준으로 대칭을 알 수 없다. 따라서 -1을 반환해야한다.
즉 짝수일경우는 대칭이든 대칭이 아니든 -1을 반환해야한다.
'''
def solution(S):
    n = len(S)
    if n == 0:
        return -1
    if n == 1:
        return 0
    if len(S)%2==0:
        return -1
    left=0
    right=n-1

    while left<right:
        if S[left]!=S[right]:
            return -1
        left+=1
        right-=1
    return left

S="racecar"
S="abba"
print(solution(S))