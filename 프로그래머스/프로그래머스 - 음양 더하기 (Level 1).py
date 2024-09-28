def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] != True:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)


absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes,signs))