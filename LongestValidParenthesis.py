"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

#=> Use a stack.

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s)==0:
        return 0
    stack = []
    i = 0
    maxLen = 0
    while i<len(s):
        #if we have '(' incoming then simply add it to the stack with its index
        if s[i]=='(':
            stack.append([i,0])     #i is the index of '(' and 0 represents that it is a '('
        #if we have ')' incoming then we have following set of rules:
        else:
            #if stack is empty or last element is ')' then stack the incoming ')'
            if len(stack)==0 or stack[-1][1]==1:
                stack.append([i,1])
            #else it means that we defenately have '(' on top of stack therefore we need to pop it out and calculate
            #current maximum valid paranthesis distance.
            else:
                stack.pop()
                if len(stack)==0:
                    currLen = i+1
                else:
                    currLen = i - stack[-1][0]
                if currLen>maxLen:
                    maxLen = currLen
        i += 1
    return maxLen

print longestValidParentheses("(())))()((()()()()()((())()()(()()(()()()(()(")