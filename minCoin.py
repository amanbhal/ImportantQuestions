"""
Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?

Examples:

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents
"""

import sys
import copy
def que(arr,target):
    if len(arr)==0:
        if target==0:
            return True
        else:
            return False
    dp = [sys.maxint for i in range(target+1)]
    dic = {}
    for i in range(len(arr)):
        dic.update({arr[i]:0})
    dp2 = [copy.deepcopy(dic) for i in range(target+1)]
    dp[0] = 0
    for i in range(1,target+1):
        for j in range(len(arr)):
            if arr[j]<=i:
                res = dp[i-arr[j]]
                if res!=sys.maxint and res+1<dp[i]:
                    dp[i] = res+1
                    for key in arr:
                        if key==arr[j]:
                            dp2[i][key] = dp2[i-arr[j]][key]+1
                        else:
                            dp2[i][key] = dp2[i-arr[j]][key]
    #print dp
    print dp2[target]
    return dp[target]
print que([3,7],13)
print que([3,7],157)