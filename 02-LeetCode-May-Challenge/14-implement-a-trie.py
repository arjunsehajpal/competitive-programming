class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_eow = False
        self.children = [None] * 26
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_inst = self
        for char in word:
            if (current_inst.children[ord(char) - ord("a")] == None):
                current_inst.children[ord(char) - ord("a")] = Trie()
            current_inst = current_inst.children[ord(char) - ord("a")]
        
        current_inst.is_eow = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_inst = self
        for char in word:
            current_inst = current_inst.children[ord(char) - ord("a")]
            if current_inst == None:
                return False
        
        if current_inst.is_eow:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_inst = self
        for char in prefix:
            current_inst = current_inst.children[ord(char) - ord("a")]
            if current_inst == None:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)