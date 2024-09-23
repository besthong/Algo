'''
You would like to set a password for a bank account. However, there are three restrictions on the format of the password:

it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
there should be an even number of letters;
there should be an odd number of digits.
You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces. The goal is to choose the longest word that is a valid password. You can assume that if there are K spaces in string S then there are exactly K + 1 words.

For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A" and "pass007". Thus the longest password is "pass007" and its length is 7. Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).

Write a function:

def solution(S)

that, given a non-empty string S consisting of N characters, returns the length of the longest word from the string that is a valid password. If there is no such word, your function should return −1.

For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7, as explained above.

Assume that:

N is an integer within the range [1..200];
string S consists only of printable ASCII characters and spaces.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


'''

'''
문제 조건에 맞게 검증해주면 된다.
1. 0-9 a-z A-Z로 이루어져있는지
2. 단어에 포함된 알파벳 문자가 짝수개인지
3. 단어에 포함된 숫자는 홀수인지

isalnum, isalpha, isdigit을 사용하면 쉽게 해결 할 수 있다.
'''

def solution(S):
    S=S.split()
    max_len = -1
    for i in S:
        if i.isalnum():
            letters = sum(c.isalpha() for c in i) #알파벳 문자의 개수
            digits = sum(c.isdigit() for c in i) #숫자의 개수

            if letters % 2 == 0 and digits % 2 == 1:
                max_len = max(max_len, len(i))
    return max_len

S="test 5 a0A pass007 ?xy1"
print(solution(S))