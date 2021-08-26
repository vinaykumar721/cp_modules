# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookAndSay(a):
    # return empty to the null input
    if not a:
        return []
    k=[]
    check= a[0]
    count=0
    for i in a:
        if i==check:
            count+=1
        else:
            check =i
            if(count>0):
                k.append(count)
            count=1
    k.append(count)
    chk=a[0]
    s=a[0]
    c=[s]
    for i in a:
        
        if(i == chk):
            continue
        else:            
            chk=i
            c.append(chk)
    z=list(zip(k,c))
    return z
