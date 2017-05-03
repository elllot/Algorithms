class TrieNode:
    def __init__(self):
        self._map = {}
        self.end = False
    
    def addChar(self, c):
        if not self.exists(c): self._map[c] = TrieNode()
    
    def delChar(self, c):
        if self.exists(c): self._map.pop(c)
    
    def exists(self, c):
        return True if c in self._map else False

    def getNext(self, c):
        return self._map[c]

    def isEmpty(self):
        return not self._map

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertWord(self, s):
        itr = self.root
        for c in s:
            itr.addChar(c)
            itr = itr.getNext(c)
        itr.end = True
        return itr

    def deleteHelper(self, s, ind, node):
        if ind == len(s):
            node.end = False
            return node.isEmpty()
        if not node.exists(s[ind]): return False
        if not self.deleteHelper(s, ind+1, node.getNext(s[ind])): return False
        node.delChar(s[ind])
        return True

    def deleteWord(self, s):
        return self.deleteHelper(s, 0, self.root)
            

    def prefixSearch(self, s):
        itr, sItr = self.root, 0
        for c in s:
            if not itr.exists(c): return None
            itr = itr.getNext(c)
        return itr
    
    def fullSearch(self, s):
        itr = self.root
        for c in s:
            if not itr.exists(c): return None
            itr = itr.getNext(c)
        if itr.end: return itr
        return None
    
    def printer(self, node, seq):
        if node.end: print(seq)
        for c in node._map:
            self.printer(node.getNext(c), seq+c)

    def printWordList(self):
        print("\nCurrent Word List:")
        print("-------------------")
        self.printer(self.root, "")
        print("-------------------\n")

myTrie = Trie()
print("inserting words...")
myTrie.insertWord("hello")
myTrie.insertWord("helloworld")
myTrie.insertWord("world")
myTrie.printWordList()
print("deleting words...")
myTrie.deleteWord("halo")
myTrie.deleteWord("hello")
myTrie.printWordList()
