# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def nth_happy_number(n):
    if n==1:
        return 1
    if n==2:
        return 7
 
    a=2;b=8
    while a<=n:
        if ishappy(b):
            a+=1
        if a==n:
            return b
        b+=1
def ishappy(m):
    while(m>=10):
        m=squarenum(m)
        if(m==1):
            return True
    return False
 
def squarenum(b):
    sum=0
    while(b>0):
        rem=b%10
        sum+=(rem*rem)
        b//=10
    return sum 