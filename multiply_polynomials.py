# Background: we can represent a polynomial as a list of its coefficients. 
# For example, [2, 3, 0, 4] could represent the polynomial 2x3 + 3x2 + 4. 
# Write the function multiplyPolynomials(p1, p2) which takes two polynomials 
# and returns a third polynomial which is the product of the two. For example,
# multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 5), and:
# (2x**22 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns [8, 10, 12, 15].

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
