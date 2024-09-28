def solution(new_id):
    answer = ''

    #  1단계 대문자 -> 소문자
    new_id = new_id.lower()

    # 2단계 : 소문자, 숫자, -, _ , . 를 제외한 모든 문자 제거
    temp = []
    for i in list(new_id):
        if i.isalpha() or i.isdigit() or i=='-' or i=='_' or i=='.':
            temp.append(i)
    new_id = ''.join(temp)

    # 3단계 : .. -> . 치환
    while '..' in new_id:
        new_id = new_id.replace('..','.')

    # 4단계 : 처음과 끝이 . 로 시작한다면 제거
    if new_id.startswith('.'): new_id = new_id.lstrip('.')
    if new_id.endswith('.'): new_id = new_id.rstrip('.')

    # 5단계 : 빈 문자열이라면 new_id 에 a대입하기
    if len(new_id) == 0: new_id = 'a'

    # 6단계 : 길이가 16자 이상일경우, 첫 15문자 제외한 나머지 모두 제거 한 후 끝 문자가 . 일 경우 .문자 제거
    new_id = new_id[:15]
    if new_id.endswith('.'): new_id = new_id.rstrip('.')

    # 7단계 : 길이가 2 이하일경우, new_id 마지막 문자를 new_id길이가 3이 될때까지 반복해서 끝에 붙이기
    if len(new_id) <= 2:
        new_id = list(new_id)
        while len(new_id) != 3:
            new_id.append(new_id[-1])
        new_id = ''.join(new_id)

    return new_id



new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = "z-+.^."
new_id = '=.='
new_id = "123_.def"
new_id = "abcdefghijklmn.p"
print(solution(new_id))