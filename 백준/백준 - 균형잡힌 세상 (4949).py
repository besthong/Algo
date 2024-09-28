import sys
import re
end = ' '
def VPS(word):
    stack=[]
    while len(word)!=0:
        if len(stack)==0:
            stack.append(word[0])
            word.pop(0)
        elif stack[-1]=='(' and word[0]==')' or stack[-1]=='[' and word[0]==']':
            stack.pop(-1)
            word.pop(0)
        else:
            stack.append(word.pop(0))
    if len(stack)==0:
        print("yes")
    else:
        print("no")
    return
while True:
    word = sys.stdin.readline().rstrip()
    if word=='.':
        break
    word=list(re.sub(r"[a-z,A-Z]","",word).replace(" ","").split(".")[0])
    VPS(word)