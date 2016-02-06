"""
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true

"""

#Method1 (Iterative)
def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    if len(p)==0:
        return len(s)==0
    #length of p is a special case
    if len(p)==1:
        if len(s)<1:
            return False
        elif s[0]!=p[0] and p[0]!='.':
            return False
        else:
            return isMatch(s[1:],p[1:])

    #if second char in p is not *
    if p[1]!='*':
        if len(s)<1:
            return False
        elif s[0]!=p[0] and p[0]!='.':
            return False
        else:
            return isMatch(s[1:],p[1:])
    #if second char in p is *
    else:
        #considering * to be 0
        if (isMatch(s,p[2:])):
            return True
        #considering * to be 1 or more than 1
        i = 0
        while i<len(s) and (s[i]==p[0] or p[0]=='.'):
            if isMatch(s[i+1:],p[2:]):
                return True
            i += 1
        return False


#Method2 (Iterative with Automata Graph)
class Node:
    def __init__(self,val,loop=False,next=None):
        self.val = val
        self.loop = loop
        self.next = next

def isMatchUsingAutomata(s,p):
    #parse the expression string i.e p and make the atomata graph
    if len(p)==0:
        return len(s)==0
    start = makeGraph(s,p)
    return match(s,start)

def makeGraph(s,p):
    start = None
    curr = None
    i = 0
    while i<len(p)-1:
        if p[i]!='*':
            if p[i+1]=='*':
                node = Node(p[i],True)
            else:
                node = Node(p[i])
            if start==None:
                start = node
                curr = node
            else:
                curr.next = node
                curr = node
        i += 1
    if i==len(p)-1 and p[i]!='*':
        node = Node(p[i])
        if start==None:
            start = node
            curr = node
        else:
            curr.next = node
            curr = node
    return start

def match(s,curr):
    #feed the string s into automata graph
    if curr==None:
        return len(s)==0
    #if there is a self loop at curr node
    if curr.loop:
        #considering * to be 0
        if match(s,curr.next):
            return True
        #considering * to be 1 or more
        i = 0
        while i<len(s) and (curr.val==s[i] or curr.val=='.'):
            if match(s[i+1:],curr.next):
                return True
            i += 1
        return False
    #if there is not a self loop at the curr node
    else:
        if len(s)<1:
            return False
        if curr.val==s[0] or curr.val=='.':
            return match(s[1:],curr.next)
        else:
            return False


#Method3 (Dynamic Programming)
def isMatchUsingDP(s,p):
    rows = len(s)
    cols = len(p)
    matrix = [[False for i in range(cols+1)] for i in range(rows+1)]

    #value of matrix[i][j] represents whether s[:i+1] is matching with p[:j+1] or not
    matrix[0][0] = True

    #initializing first row
        #It can be true only if currently it is a star char and it is true before the star char
    for i in range(2,cols+1):   #star chars can only start from 2nd position
        matrix[0][i] = matrix[0][i-2] and p[i-1]=='*'

    #filling rest of the matrix
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            #if p[j-1] is not star
                #if chars at p[j-1]==s[i-1] or p[j-1]=="." then matrix[i][j] should be same as matrix[i-1][j-1]
            if (p[j-1]==s[i-1] or p[j-1]==".") and matrix[i-1][j-1]:
                matrix[i][j] = True
                continue
            #if p[j-1] is star
            if p[j-1]=="*" and j>1:
                #considering * to be zero i.e. matrix[i][j] should be equal to matrix[i][j-2]
                if matrix[i][j-2]:
                    matrix[i][j] = True
                    continue
                #considering * to be one or more
                    #for that char having star should match the string s char and matrix[i-1][j] i.e. it should
                    #also match the previos string versions
                if (p[j-2]==s[i-1] or p[j-2]==".") and matrix[i-1][j]:
                    matrix[i][j] = True
                    continue

    for i in range(len(matrix)):
        print matrix[i]
    return matrix[rows][cols]


#print isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c")
#print isMatchUsingAutomata("a","ab*")
'''print isMatchUsingAutomata("abcwxyz",".*xyz")
print isMatchUsingAutomata("abcwxyz",".*")
print isMatchUsingAutomata("ab",".*c")
print isMatchUsingAutomata("aaa","a.a")
print isMatchUsingAutomata("aaa","a*a")
print isMatchUsingAutomata("aaa","aaaa")'''
#print isMatchUsingAutomata("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c")
#print isMatchUsingDP("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c")
print isMatchUsingDP("aaa","a*a")