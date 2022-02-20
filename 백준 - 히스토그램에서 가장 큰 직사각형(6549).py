import math,sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def segmentTree(temp,tree,node,start,end):  # temp,tree,1,0,len(temp)-1

    if start==end:
        tree[node-1] = start
    else:
        mid = (start+end)//2
        segmentTree(temp,tree,node*2,start,mid)
        segmentTree(temp,tree,node*2+1,mid+1, end)

        # 부모노드에 더 작은 자식노드 입력
        if temp[tree[node*2-1]] < temp[tree[node*2]]:
            tree[node-1] = tree[node*2-1]
        else:
            tree[node-1] = tree[node*2]

# 구간 최솟값 찾기
def query(temp,tree,node,start,end,x,y):
    #주어진 범위가 전체 범위를 벗어난경우
    if x > end or y < start:
        return -1
    #줭진 범위가 전체 범위 안에 포함되는경우
    if start >= x and end <= y:
        return tree[node-1]

    mid = (start+end)//2
    left = query(temp,tree,node*2,start,mid,x,y)
    right = query(temp,tree,node*2+1, mid+1, end, x,y)

    #한쪽 노드가 범위를 벗어난 경우 반대쪽 노드 선택
    if left==1:
        return right
    elif right == -1:
        return left
    else:
        #더 작은 값의 인덱스 선택
        if temp[left] >= temp[right]:
            return right
        else:
            return left

def ans(start,end):
    #해당 구간 범위 최소값 인덱스 구하기
    index = query(temp,tree,1,0,len(temp)-1,start,end)
    if abs(end-start)==0:
        return temp[index]

    a,b,c = temp[index] * (end-start+1),0,0

    if index-1 >= start:
        b = ans(start,index-1)
    if index+1 <= end:
        c = ans(index+1,end)
    return max(a,b,c)
while True:
    temp = list(map(int,input().split()))
    if temp[0]==0:
        break
    else:
        case = temp.pop(0)
    tree = [0]*(pow(2,math.ceil(math.log(len(temp),2))+1)-1)

    segmentTree(temp,tree,1,0,len(temp)-1)
    print(ans(0,len(temp)-1))
'''
스택 이용
while True:
    temp = list(map(int,input().split())) # temp = 2,1,4,5,1,3,3
    if temp[0] == 0:
        break
    else:
        case = temp.pop(0)
    stack=[]
    answer=0
    for i in range(case):
        while len(stack)!=0 and temp[stack[-1]] > temp[i]:
            tmp = stack.pop()
            if len(stack)==0:
                width = i
            else:
                width = i - stack[-1] -1
            answer = max(answer,width * temp[tmp])
        stack.append(i)

    while len(stack)!=0:
        tmp = stack.pop()

        if len(stack)==0:
            width = case
        else:
            width = case - stack[-1] -1
        answer = max(answer,width * temp[tmp])
    print(answer)
'''