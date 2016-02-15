"""
Get maximum binary Gap.

For example, 9's binary form is 1001, the gap is 2.
"""

#=> Using Bit Manipulation
#=> The key to solve this problem is the fact that an integer x & 1 will get the last digit of the integer.

def maximumGap(nums):
    maxGap = 0
    currGap = -1    #initialized with -1 because only 1 will reset it to 0 and then gap counting will start i.e.
                    #we need to count only those zeros which are between 1s.
    lastBit = 0
    while nums>0:
        lastBit = nums & 1
        nums = nums >> 1
        if lastBit==0 and currGap>=0:
            currGap += 1
        if lastBit==1:
            if currGap>maxGap:
                maxGap = currGap
            currGap = 0
    return maxGap

print maximumGap(9)