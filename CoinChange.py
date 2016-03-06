"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""


#=> Backtracking method O(c^n), c = length of coins array and n = amount
def coinChange1(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    global count
    count = 0
    changeAux(coins,amount)
    return count

def changeAux(coins,amount):
    global count
    if amount==0:
        return 0
    if amount in coins:
        count += 1
        return 1
    if amount<sorted(coins)[0]:
        return -1
    for coin in sorted(coins,reverse=True):
        if amount-coin>=0:
            count += 1
            result = changeAux(coins,amount-coin)
            if result!=-1:
                return 1
            count -= 1
    return -1

#=> Using Dynamic Programming O(c*n), c = length of coins array and n = amount
def coinChange2(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    maxAmount = amount+1
    dp = [maxAmount for i in range(amount+1)]
    dp[0] = 0
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i] = min(dp[i],dp[i-coin]+1)
    if dp[amount]>amount:
        return -1
    return dp[amount]

print coinChange([1,2,3],7)