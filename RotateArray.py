"""
Problem: Rotate an array of n elements to the right by k steps. For example, with n = 7
and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. How many different
ways do you know to solve this problem?
"""

#Method1
#using auxilary array
#time: O(n) space: O(n)
def rotate_1(A,k):
    result = [None for i in range(len(A))]
    for i in range(len(A)):
        result[(i+k)%len(A)] = A[i]
    print result

rotate_1([1,2,3,4,5,6,7,8,9],3)

#Method2
#using bubble sort kind of thing, the main idea is to bring last k elements to the front
#time: O(n*k) space: O(1)
def rotate_2(A,k):
    for i in range(k):
        for j in range(len(A)-1,0,-1):
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp
    print A

rotate_2([1,2,3,4,5,6,7,8,9],3)

#Method3
#example:
#[1,2,3,4,5,6,7,8,9] with k=3
#divide list into two parts one of length n-k and other of length k
#=> [1,2,3,4,5,6]   [7,8,9]
#reverse both lists individually
#=> [6,5,4,3,2,1]   [9,8,7]
#join both lists and then rotate the whole list
#=> [6,5,4,3,2,1,9,8,7]
#=> [7,8,9,1,2,3,4,5,6]
#time: O(n) Space: O(n)
def rotate_3(A,k):
    n = len(A)
    A = customReverse(A[:n-k])+A[n-k:]
    A = A[:n-k]+customReverse(A[n-k:])
    A.reverse()
    print A

def customReverse(A):
    start = 0
    end = len(A)-1
    while start<=end:
        temp = A[start]
        A[start] = A[end]
        A[end] = temp
        start += 1
        end -= 1
    return A

rotate_3([1,2,3,4,5,6,7,8,9],3)