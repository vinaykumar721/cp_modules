def fun_nth_additive_prime(n):
   if(n == 0):
       return 2
   elif(n == 1):
       return 3
   x = 1
   y = 4
   while(x<=n):
       if(additivePrime(y)):
           x = x+1
       if(x == n):
           return y
       y = y+1
 
def additivePrime(n):
   if(isPrime(n) and isPrime(sumDigit(n))):
       return True
 
def sumDigit(n):
   sum = 0
   while(n!=0):
       sum = sum + n%10
       n = n//10
   return sum
 
def isPrime(n):
   if (n < 2):
       return False
   if (n == 2):
       return True
   if (n % 2 == 0):
       return False
   maxFactor = round(n**0.5)
   for factor in range(3,maxFactor+1,2):
       if (n % factor == 0):
           return False
   return True
