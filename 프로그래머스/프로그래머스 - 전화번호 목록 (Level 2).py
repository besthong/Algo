def solution(phone_book):
    answer = True
    ph = sorted(phone_book)

    for i in range(1,len(ph)):
        if ph[i].startswith(ph[i-1]):
            return False
        else:
            answer = True
    return answer


'''
["123","456","789"]
["12","123","1235","567","88"]
["119", "97674223", "1195524421"]
'''
phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))