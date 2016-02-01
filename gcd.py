"""
Lets say g is gcd(m, n) and m > n.

m = g * m1
n = g * m2

m - n = g * (m1 - m2)

gcd (m, n) = gcd(m-n, n)    this can be done more than once
Use this to solve the question
"""
# time: O(a) Space: O(1)
def gcd(A,B):
    if A==0:
        return B
    if B==0:
        return A
    n = max(A,B)/min(A,B)
    a = max(A,B)-(n*min(A,B))
    if a==0:
        return min(A,B)
    for i in range(min(a,min(A,B)),0,-1):
        if A%i==0 and B%i==0:
            return i

print gcd(4,9)