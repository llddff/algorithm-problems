from LeetCode刷题.Leet208 import TrieNode


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word):
        curr = self.root

        def helper(node, word_, index):
            if index == len(word_):
                return node.is_word
            cur_node = node
            ch = word_[index]
            if ch == '.':
                for c_node in cur_node.children.values():
                    if helper(c_node, word_, index + 1):
                        return True
                return False
            else:
                cur_node = cur_node.children.get(ch)
                if not cur_node:
                    return False
                return helper(cur_node, word_, index + 1)

        return helper(curr, word, 0)
