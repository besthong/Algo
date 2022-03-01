a,b,c = map(int,(input().split()))
def multi(a,b):
    if b==1:
        return a%c
    else:
        temp = multi(a,b//2)
        if b%2==0:
            return (temp*temp)%c
        else:
            return (temp*temp*a)%c
print(multi(a,b))