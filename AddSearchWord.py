class Node:
    def __init__(self,val):
        self.val = val
        self.links = [None for i in range(27)]

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = Node(None)
        self.lookUp = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,'STOP':26}
        #self.curr = self.root

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        word = list(word)
        word.append("STOP")
        #self.curr = self.root
        curr = self.root
        for i in range(len(word)):
            if curr.links[self.lookUp[word[i]]]==None:
                x = Node(word[i])
                curr.links[self.lookUp[word[i]]] = x
                curr = curr.links[self.lookUp[word[i]]]
            else:
                curr = curr.links[self.lookUp[word[i]]]
        #self.curr = self.root



    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        word = list(word)
        word.append("STOP")
        curr = self.root
        return self.dfs_search(word,curr,0)

    def dfs_search(self,word,curr,ptr):
        if ptr==len(word):
            return curr.val=="STOP"
        if curr.val=="STOP":
            return False
        if word[ptr]=='.':
            for j in range(27):
                if curr.links[j]!=None:
                    if self.dfs_search(word,curr.links[j],ptr+1):
                        return True
        elif curr.links[self.lookUp[word[ptr]]]!=None:
            return self.dfs_search(word,curr.links[self.lookUp[word[ptr]]],ptr+1)
        return False


#Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# print wordDictionary.search("....")
wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")
print wordDictionary.search("a")
print wordDictionary.search(".at")
wordDictionary.addWord("bat")
print wordDictionary.search(".at")
print wordDictionary.search("an.")
print wordDictionary.search("a.d.")
print wordDictionary.search("b.")
print wordDictionary.search("a.d")
print wordDictionary.search(".")