def solution(p,l):
    loc = [i for i in range(len(p))]
    final_loc=[]
    while len(p)!=0:
        if p[0] == max(p):
            final_loc.append(loc.pop(0))
            p.pop(0)
        else:
            p.append(p.pop(0))
            loc.append(loc.pop(0))
    return final_loc.index(l)+1
# p = [2,1,3,2]
# l = 2
p = [2,3,3,2,9,3,3]
l = 3
# p = [1,1,9,1,1,1]
# l = 0
print(solution(p,l))
