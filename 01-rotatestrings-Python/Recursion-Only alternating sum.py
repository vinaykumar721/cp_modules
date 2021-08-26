def fun_recursions_alternatingsum(l): 
    if len(l)==0:
        return 0
    else:
        result= l[0] - fun_recursions_alternatingsum(l[1:])
        return result

def readList():
    a=[]
    l=int(input())
    for i in range(l):
        a.append(int(input()))
    return a

