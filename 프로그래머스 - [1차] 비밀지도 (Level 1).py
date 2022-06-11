'''
bin, or 연산을사용해 쉽게 풀 수 있지만
다른사람 풀이를 보면 bin후 바로 or연산적용이 가능하다.
최대한 한번에 구현하고자 노력하였지만 아직 갈길이 멀다.
'''

#다른사람 풀이
def solution(n,arr1,arr2):
    answer=[]
    for i,j in zip(arr1,arr2):
        a12 = bin(i|j)[2:]
        a12 = a12.rjust(n,'0')
        a12 = a12.replace('1','#')
        a12 = a12.replace('0',' ')
        answer.append(a12)
    return answer


#내 풀이..
def solution(n, arr1, arr2):
    answer = []

    for i,j in zip(arr1,arr2):
        arr1_bin = list(map(int,list(bin(i)[2:].zfill(n))))
        arr2_bin = list(map(int,list(bin(j)[2:].zfill(n))))

        temp=[]
        for z in range(n):
            temp.append(arr1_bin[z] or arr2_bin[z])

        answer.append(''.join(list(map(str,temp))))
    realans=[]
    for i in answer:
        i=i.replace('1','#').replace('0',' ')
        realans.append(i)
    return realans


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n,arr1,arr2))
'''
["#####","# # #", "### #", "# ##", "#####"]
'''
