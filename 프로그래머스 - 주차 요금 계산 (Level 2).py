import math
def solution(fees,records):
    s = {}

    for record in records:
        time,number,status = record.split()
        time = time.split(':')
        time = int(time[0])*60 + int(time[1])

        if number not in s:
            s[number] = (0,time,status)
        if status == 'IN':
            s[number] = (s[number][0], time, status)
        elif status == 'OUT':
            total_time, in_time, _ = s[number]
            total_time += time- in_time
            s[number] = (total_time, time, status)

    result={}
    for key in s.keys():
        total_time, time, status = s[key]
        if status=='IN':
            total_time += 1439-time
            s[key] = total_time,time,status
        if total_time<fees[0]: # 토탈시간이 기본시간보다 적을경우
            result[key]=fees[1]
        else:
            result[key] = fees[1] + math.ceil((total_time-fees[0])/fees[2]) * fees[3]

    return list(map(lambda x:x[1], sorted(result.items())))


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN",
           "06:00 0000 IN",
           "06:34 0000 OUT",
           "07:59 5961 OUT",
           "07:59 0148 IN",
           "18:59 0000 IN",
           "19:09 0148 OUT",
           "22:59 5961 IN",
           "23:00 5961 OUT"]
print(solution(fees,records))
