import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            curr = curr.children.get(c)
            if not curr:
                return False
        return curr.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            curr = curr.children.get(c)
            if not curr:
                return False
        return True
