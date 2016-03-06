"""
Given an unsorted array of positive integers. Find the number of triangles that can be formed with three different
array elements as three sides of triangles. For a triangle to be possible from 3 values, the sum of any two values
(or sides) must be greater than the third value (or third side).
For example, if the input array is {4, 6, 3, 7}, the output should be 3. There are three triangles possible {3, 4, 6},
{4, 6, 7} and {3, 6, 7}. Note that {3, 4, 7} is not a possible triangle.
As another example, consider the array {10, 21, 22, 100, 101, 200, 300}. There can be 6 possible triangles: {10, 21, 22}
, {21, 100, 101}, {22, 100, 101}, {10, 100, 101}, {100, 101, 200} and {101, 200, 300}
"""


#=> Method1 using BackTracking.
#   Make all possible combinations of triangle sides and increase the result only for qualifying sides.
#   O(2^N)

def countTriangles1(arr):
    # arr: List[int]
    # rType: int
    if len(arr)==0 or len(arr)<3:
        return 0
    result = [0]
    item = []
    dfs(result,item,arr,3,0)
    print result[0]

def dfs(result,item,n,k,i):
    if len(item)==k:
        if item[0]+item[1]>=item[2] and item[0]+item[2]>=item[1] and item[1]+item[2]>=item[0]:
            result[0] += 1
        return
    for j in range(i,len(x)):
        item.append(x[j])
        dfs(result,item,n,k,j+1)
        item.pop()

#=> Method2 by sorting and then using two pointers.
#   O(N^3)

def countTriangle2(arr):
    #arr: List[int]
    #rType: int
    if len(arr)==0 or len(arr)<3:
        return 0
    arr.sort()
    ptr1 = 0
    ptr2 = 1
    ptr3 = None
    result = 0
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)):
            k = j+1
            while k<len(arr) and arr[i]+arr[j]>=arr[k]:
                result += 1
                k += 1
    return result

print countTriangle2([6,4,9,7,8])
