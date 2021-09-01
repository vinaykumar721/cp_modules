# Background:  in Chess, a King can move from any square to
# any adjacent square.  A King’s Tour is a series of legal King
# moves so that every square is visited exactly once. 
# We can represent a Kings Tour in a 2d list where the 
# numbers represent the order the squares are visited, going 
# from 1 to N2.  For example, consider these 2d lists:

#    [ [  3, 2, 1 ],    	[ [  1, 2, 3 ],  	[ [ 3, 2, 1 ],
#  	[  6, 4, 9 ],      	[  7, 4, 8 ],    	[ 6, 4, 0 ],
#  	[  5, 7, 8 ] ]     	[  6, 5, 9 ] ]   	[ 5, 7, 8 ] ]

# The first is a legal Kings Tour but the second is not, 
# because there is no way to legally move from the 7 to the 8, 
# and the third is not, because it contains a 0 which is out
#  of range.  With this in mind, write the function 
# isKingsTour(board) that takes a 2d list of integers, 
# which you may assume is NxN for some N>0, and 
# returns True if it represents a legal Kings Tour 
# and False otherwise.

def isKnightsTour(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if (board[x][y] == 0):
                return False
    i=1
    while(i<(len(board)*len(board[0]))):
        r1,c1 = rowcol(board,i)
        r2,c2 = rowcol(board,(i+1))
        if(r1 == -1) or (c1 == -1):
            return False
        i+=1
        if(isvalidmove(r1,c1,r2,c2) == False):
            return False
    return True 
 
def isvalidmove(r1,c1,r2,c2):
    if((abs(r1-r2)==1)and(abs(c1-c2)==2))or((abs(c1-c2)==1)and(abs(r1-r2)==2)):
        return True
    return False
 
def rowcol(board,i):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if (board[x][y] == i):
                return x,y
    return (-1,-1)
 
board = [
            [  1, 60, 39, 34, 31, 18,  9, 64 ],
            [ 38, 35, 32, 61, 10, 63, 30, 17 ],
            [ 59,  2, 37, 40, 33, 28, 19,  8 ],
            [ 36, 49, 42, 27, 62, 11, 16, 29 ],
            [ 43, 58,  3, 50, 41, 24,  7, 20 ],
            [ 48, 51, 46, 55, 26, 21, 12, 15 ],
            [ 57, 44, 53,  4, 23, 14, 25,  6 ],
            [ 52, 47, 56, 45, 54,  5, 22, 13 ],
        ]
assert(isKnightsTour(board)==True)
# You can write your own test cases here...
print("All test cases passed....")
