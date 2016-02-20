"""
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On
the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the nth round,
you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3.

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
"""

#=> for each bulb we need to count it's number of factors. If the no.of factors are odd then bulb is on else off.

#=> a number has odd number of factors only if it is a square root. Therefore we just need to find the number of
#   indexes which are perfect squares.

#=> We need to find the maximum perfect square less than n and sqrt(n) will be the answer.
#=> We can use binary search to find a number whose sqaue is just less than n.

import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        left = 1
        right = n
        while left<=right:
            mid = left + (right-left)/2
            if mid*mid==n:
                return mid
            elif mid*mid<n and (mid+1)**2>n:
                return mid
            elif mid**2>n:
                right = mid-1
            else:
                left = mid+1

instance = Solution()
print instance.bulbSwitch(9999999)