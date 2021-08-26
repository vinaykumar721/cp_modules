# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)


def isprime(l):
    if (l <= 1):
        return False
    if (l == 2):
        return True
    if (l % 2 == 0):
        return False
    maxFactor = round(l**0.5)
    for factor in range(3,maxFactor+1,2):
        if (l % factor == 0):
            return False
    return True
 
def squarenum(b):
    sum=0
    while(b>0):
        rem=b%10
        sum+=(rem*rem)
        b//=10
    return sum  
 
def ishappy(m):
    while(m>=10):
        m=squarenum(m)
        if(m==1):
            return True
    return False
 
def fun_nth_happy_prime(n):
    if(n==0):
        return 7
    count=0
    x=7
    while True:
        if(isprime(x) and ishappy(x)):
            count+=1
        if(count==n):
            return x
        x+=1
