"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""

#=> use the first row and first col to store whether there is zero at a place matrix[i][j]
#=> while retrieving the information set matrix[i][j]=0 if either the corresponding first row or col has a zero.

def setZeroes(matrix):
    firstColZero = False
    firstRowZero = False

    #check zeros in first row
    for i in range(len(matrix[0])):
        if matrix[0][i]==0:
            firstRowZero = True

    #check zeros in first col
    for i in range(len(matrix)):
        if matrix[i][0]==0:
            firstColZero = True

    #record zeros in first col and row
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j]==0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    #retrieve information from first row and col
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j] = 0
    if firstRowZero:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0

    if firstColZero:
        for i in range(len(matrix)):
            matrix[i][0] = 0

