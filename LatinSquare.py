# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    a=[]
    h=0
    if len(lst)== len(lst[0]):
        for i in range(len(lst)):
            for j in range(len(lst)):
                a.append(lst[i][j])
            break
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] in a and lst[i][j] in a:
                continue
            else:
                return False
    return True