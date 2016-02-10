"""
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of
elements in both subsets is same.

Examples

arr[] = {1, 5, 11, 5}
Output: true
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false
The array cannot be partitioned into equal sum sets.
"""

#=> Dynamic Programming
#   if the sum of all the elements is odd then return false.
#   matrix[i][j] is true if {a[0],a[1],...,a[j-1]} has a subset that has the sum equal to i else false.
#   each element has two choices whether it is included in the subset or not therefore
#   matrix[i][j] = matrix[i][j](not-included) or matrix[i-arr[j-1]][j-1](included)

def partition(arr):
    if len(arr)==0:
        return False
    #calculate sum of all elements
    arrSum = sum(arr)
    print arrSum
    if arrSum%2!=0:
        return False
    matrix = [[None for i in range(len(arr)+1)] for i in range((arrSum/2)+1)]

    #first row is all true.
    for i in range(len(arr)+1):
        matrix[0][i] = True

    #first col is all false except 0,0
    for i in range(1,(arrSum/2)+1):
        matrix[i][0] = False

    #fill rest of the matrix
    for i in range(1,(arrSum/2)+1):
        for j in range(1,len(arr)+1):
            #j element not included in the subset
            matrix[i][j] = matrix[i][j-1]
            if i>=arr[j-1]:
                #j element included in the subset
                matrix[i][j] = matrix[i][j] or matrix[i-arr[j-1]][j-1]

    return matrix[arrSum/2][len(arr)]

print partition([3, 1, 1, 2, 2,1])