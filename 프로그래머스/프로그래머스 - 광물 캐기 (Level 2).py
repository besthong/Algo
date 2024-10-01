'''
해당 문제는 그리디 풀이가 가능하다.
먼저 곡괭이당 5개의 광물을 캘 수 있으므로, minerals를 5개씩 그룹화 하고 계산하면 쉽게 풀 수 있다.
'''
def solution(picks,minerals):
    answer=0
    group = {"diamond":0, "iron":0, "stone":0}
    dict = {0: (1, 1, 1), 1: (5, 1, 1), 2: (25, 5, 1)}


    length = min(sum(picks)*5, len(minerals))
    temp=[]

    for i in range(length):
        group[minerals[i]] += 1
        if (i+1)%5==0 or i == len(minerals)-1: # 5번째에서 짜르거나, 마지막까지 갔을때는 계산 및 초기화
            temp.append([group["diamond"],group["iron"],group["stone"]])
            group["diamond"], group["iron"], group["stone"] = 0,0,0

    temp.sort(key=lambda x:(x[0],x[1],x[2]),reverse=True)

    for dia, iron, stone in temp: #다이아 개수 * 다이아 dict
        for i in range(3):
            if picks[i]:
                picks[i]-=1
                answer += dia*dict[i][0] + iron * dict[i][1] + stone * dict[i][2]
                break
    return answer
picks = [1,3,2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

print(solution(picks,minerals))
