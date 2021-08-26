"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    input_array.sort()
    first=0
    last = len(input_array)-1
    while first <= last:
        mid = (last+first)//2
        if input_array[mid] == value:
            return mid
        elif(value < input_array[mid]):
            last = mid-1
        else:
            first=mid+1
    return -1

