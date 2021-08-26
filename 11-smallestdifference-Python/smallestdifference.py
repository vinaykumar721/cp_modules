# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
    # return empty to the null input
    if not a:
        return []
    k=[]
    check= a[0]
    count=0
    # checking for the dupilcate values and counting them 
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
    # list the values of repeated to invidual.
    for i in a:
        
        if(i == chk):
            # c.append(s)
            continue
        else:            
            chk=i
            c.append(chk)
    
    # print(c)
    # print(a)
    # print(k)
    z=list(zip(k,c))
    return z
