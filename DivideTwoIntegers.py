"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

#=> O(n) solution
def divide1(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if divisor==0:
        return 0
    count = 0
    if dividend<0 and divisor<0:
        dividend = abs(dividend)
        divisor = abs(divisor)
    negative = False
    if dividend<0 or divisor<0:
        dividend = abs(dividend)
        divisor = abs(divisor)
        negative = True
    if dividend<divisor:
        return 0
    while dividend>=divisor:
        count += 1
        dividend -= divisor
    if negative:

        return -count
    else:
        return count

#=> O(logN) solution using bit manipulation

def divide2(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    #handle divide with zero
    if divisor==0:
        return sys.maxint
    #if dividend is MIN_INT and divisor is -1 then return MAX_INT
    if dividend<=-2147483648 and divisor==-1:
        return 2147483647
    negative = False
    #if either dividend or divisor is 0, but not both, then assign negative to be True
    if (dividend<0)^(divisor<0):
        negative = True
    #convert both dividend and divisor to positive as we have already handled the -ive sign in previous step
    dividend = abs(dividend)
    divisor = abs(divisor)
    result = 0
    while dividend>=divisor:
        temp = divisor
        multiple = 1
        #keep on dividing dividend from temp until dividend<(temp<<1) every time we divide dividend with temp the
        #multiple increases twice because of the left shifting.
        while dividend>=(temp<<1):
            temp = temp<<1
            multiple = multiple<<1
        dividend -= temp
        result += multiple
    remainder = dividend
    if negative:
        return -result,-remainder
    else:
        return result,remainder

print divide2(-2147483648,-1)
print divide2(1347624,453)
print divide2(-4620836,762)