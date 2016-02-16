"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s)==0:
        return True
    s = s.lower()
    left = 0
    right = len(s)-1
    while left<=right:
        if s[left].isalnum() and s[right].isalnum():
            if s[left]==s[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
        if s[left].isalnum()==False:
            left += 1
        if s[right].isalnum()==False:
            right -= 1
    return True

print isPalindrome("A man, a plan, a canal: Panama")