"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
 Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]


You should return [1,2,3,6,9,8,7,4,5].

"""

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if len(matrix)==0:
        return []
    right = True
    down = False
    left = False
    up = False
    rightEnd = len(matrix[0])-1
    downEnd = len(matrix)-1
    leftEnd = 0
    upEnd = 1
    noOfElements = len(matrix)*len(matrix[0])
    countElements = 0
    i = 0
    j = 0
    result = []
    while countElements<noOfElements:
        if right:
            if j<=rightEnd:
                result.append(matrix[i][j])
                j += 1
                countElements += 1
            else:
                right = False
                down = True
                j = rightEnd
                i += 1
                rightEnd -= 1
        elif down:
            if i<=downEnd:
                result.append(matrix[i][j])
                i += 1
                countElements += 1
            else:
                down = False
                left = True
                i = downEnd
                j -= 1
                downEnd -= 1
        elif left:
            if j>=leftEnd:
                result.append(matrix[i][j])
                j -= 1
                countElements += 1
            else:
                left = False
                up = True
                j = leftEnd
                i -= 1
                leftEnd += 1
        elif up:
            if i>=upEnd:
                result.append(matrix[i][j])
                i -= 1
                countElements += 1
            else:
                up = False
                right = True
                i = upEnd
                j += 1
                upEnd += 1
    return result

print spiralOrder([[1,2,3],[4,5,6],[7,8,9]])