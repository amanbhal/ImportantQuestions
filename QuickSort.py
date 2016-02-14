"""
Design Quick Sort algorithm to sort an integer array.
"""

def quicksort(arr):
    if len(arr)==0:
        return []
    helper(arr,0,len(arr)-1)
    print arr

def helper(arr,start,end):
    if start>=end:
        return
    middle = (start+end)/2
    pivot = arr[middle]
    left = start
    right = end
    while left<=right:
        while arr[left]<pivot:
            left += 1
        while arr[right]>pivot:
            right -= 1
        if left<=right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    helper(arr,start,right)
    helper(arr,left,end)

quicksort([3,5,2,4,1])