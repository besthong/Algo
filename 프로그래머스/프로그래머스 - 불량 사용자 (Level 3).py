'''
문자열의 조합을 전부 계산하여, banned_id 와 일치하는지의 여부를 찾는다.
만약 일치한다면 possible_combinations 리스트에 적재한다. 이 때 적재는 frozenset의 형태로 적재한다.
이유는 이 후 마지막 단게에서 한번 더 중복을 제거해야하기때문이다.
만약 해당 단계에서 set의 형태로 중복제거 후 적재했다면
a=[set(), set(), ... ] 의 형태가 됐을텐데, 다시 한번 이 형태를 중복제거하려 set()을 사용한다면
에러가 발생한다. set은 가변객체이기때문이다.
따라서 데이터 적재시에 바로 frozenset을 사용하여 적재한다. 이는 불변객체이기때문에 한번 더 set을 통해
중복 제거가 가능하다.
'''
from itertools import permutations
def is_match(id, ban_id):
    if len(id)!=len(ban_id): return False #길이 안맞는경우 False 반환

    for i,j in zip(id,ban_id):
        if i!=j and j!='*':
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    possible_combinations=[]
    for perm in permutations(user_id, len(banned_id)):
        if all(is_match(perm[i], banned_id[i]) for i in range(len(banned_id))):
            # 중복을 피하기 위해 set으로 저장
            possible_combinations.append(frozenset(perm))

    unique_possible = set(possible_combinations)
    return len(unique_possible)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id=["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))