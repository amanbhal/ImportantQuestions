"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""

#=> Idea is that first we strip the string of whitespaces and then we replace multiple spaces with single space.
#=> Then we reverse every word seperated with a whitespace. example: "the sky blue" -> "eht yks eulb"
#=> Finally we reverse the whole string which we get after reversing each word. example: "eht yks eulb" -> "blue sky
#   the"

import re
def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s)==0:
        return ""
    #if there is no space i.e. the string is one word then simply return the string
    if s.count(" ")==0:
        return s
    #strip whitespaces from beginning and last of the string
    s = s.strip()
    #if len is zero after string the return empty string
    if len(s)==0:
        return ""
    #substitute multiple spaces with single space
    s = re.sub(" +"," ",s)
    #add space in starting and ending so that the first and last word is reversed
    s = " "+s+" "
    global x
    x = list(s)
    #reverse the string between left and right pointer
    left = -1
    right = -1
    curr = 0
    while curr<len(s):
        if x[curr]==" ":
            if left!=-1 and right==-1:
                right = curr
            if left==-1:
                left = curr
            if left!=-1 and right!=-1:
                reverse(left+1,right-1)
                #reset left and right after reversing
                left = -1
                right = -1
            else:
                curr += 1
        else:
            curr += 1
    x.pop(0)
    x.pop(-1)
    x.reverse()
    x = "".join(x)
    return x

def reverse(start,end):
    global x
    while start<=end:
        x[start], x[end] = x[end], x[start]
        start += 1
        end -= 1

print reverseWords("the sky is blue")