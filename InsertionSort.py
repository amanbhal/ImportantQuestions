"""
Implement Insertion Sort on an array.
"""

def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i
        while(j>0 and arr[j]<arr[j-1]):
            print i,j,
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
            print arr
    return arr

print insertionSort([6,5,4,3,2,1])