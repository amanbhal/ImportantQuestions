"""
Find the largest subarray with equal number of 0s and 1s.
example:
0 0 1 0 1 0 1 0 1
Output: 8, [0 1 0 1 0 1 0 1]
"""

def largestSetOfZeroAndOne(arr):
    if len(arr)==0:
        return 0,[]
    countOnes = arr.count(1)
    countZeros = arr.count(0)
    i = 0
    j = len(arr)-1
    while i<j:
        if countOnes==countZeros:
            break
        elif countOnes>countZeros:
            if arr[i]==1:
                i += 1
                countOnes -= 1
            elif arr[j]==1:
                j -= 1
                countOnes -= 1
            else:
                i += 1
                countZeros -= 1
        else:
            if arr[i]==0:
                i += 1
                countZeros -= 1
            elif arr[j]==0:
                j -= 1
                countZeros -= 1
            else:
                j -= 1
                countOnes -= 1
    return j-i+1,arr[i:j+1]

print largestSetOfZeroAndOne([0,0,1,0,1,0,1,0,1])
print largestSetOfZeroAndOne([1,1,1,1,1,0,0,0,0,0,0,0,1])