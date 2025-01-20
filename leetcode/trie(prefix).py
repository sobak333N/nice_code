class TrieNode:

    def __init__(self):
        self.childrens: dict = {}
        self.end_of_word: bool = False

class Trie:

    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root
        
        for char in word:
            if char not in cur_node.childrens:
                new_node = TrieNode()
                cur_node.childrens[char] = new_node
            cur_node = cur_node.childrens[char]

        cur_node.end_of_word = True


    def search(self, word: str) -> bool:
        cur_node = self.root
        for char in word:
            if char not in cur_node.childrens:
                return False
            cur_node = cur_node.childrens[char]
        
        return cur_node.end_of_word


    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.childrens:
                return False
            cur_node = cur_node.childrens[char]
        
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)