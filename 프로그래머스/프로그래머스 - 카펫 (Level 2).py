def solution(brown, yellow):
    answer = []
    gcd_list=[]
    middle=0
    sum=brown+yellow
    for i in range(1,sum+1):
        if sum%i==0:
            gcd_list.append(i)
    print(gcd_list)

    if len(gcd_list)%2!=0:
        gcd_list.append(gcd_list[len(gcd_list)//2])
        gcd_list=sorted(gcd_list)
    size = len(gcd_list)
    for x in range(size//2):
        if (int(gcd_list[x])-2)*(int(gcd_list[(size-1)-x])-2)==yellow:
            answer.append(gcd_list[(size-1)-x])
            answer.append(gcd_list[x])
    return answer