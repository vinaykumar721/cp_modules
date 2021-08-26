# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def multipolynomials(p1, p2):
    q=len(p1)
    r=len(p2)
    c=[]
    m=0
    if(q==r==0):
        return None
    while(m<len(p1)):
        for i in range(len(p2)):
            if(p1[m]*p2[i]!=0):
                c.append(p1[m]*p2[i])
        m+=1
    return c



