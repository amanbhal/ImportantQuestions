"""
String encoding-decoding question. Given a digit sequence, return no. of ways it can be decoded.
Mapping : A->1, B->2, Z->26
For ex : Given a string "123", based on the mapping it can be decoded to following ways :-
(1) 1,2,3 -> A,B,C (2) 12,3 -> L,C (3) 1,23 -> A,W
"""

#=> Using Dynamic Programming
#       every number can either be single or paired with the previous number. We are pairing only two because maximum
#       number can be 26 that corresponds to Z.
#       matrix[i] = matrix[i-1](taking single)+matrix[i-2](coupling with previous number)

def encodeDecode(str):
    arr = list(str)
    dp = [None for i in range(len(arr)+1)]

    #dp[0] will be 1 because null string can be encoded in only one way.
    dp[0] = 1

    dp[1] = 1   #because single letter can be encoded in only one way.

    for i in range(2,len(dp)):
        if arr[i-1]=='0':   #if current number is zero then there is only one method viz to join it with previous
                            #number ex: "101" we have to interpret it as 10,1
            ways1 = 0
        else:
            ways1 = dp[i-1]
        if arr[i-2]=='0':   #if the previous number is 0 then there is no use to couple it with current number
                            #because 09 is equivalent to 9.
            ways2 = 0
        else:
            couple = arr[i-2]+arr[i-1]
            couple = int(couple)
            ways2 = 0
            if couple>0 and couple<27:
                ways2 = dp[i-2]
        dp[i] = ways1 + ways2

    return dp[-1]

print encodeDecode("122222")
print encodeDecode("123")
print encodeDecode("899")
print encodeDecode("101")