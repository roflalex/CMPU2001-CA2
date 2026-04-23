from trie.trie_node import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,title:str, movie: dict):
        node = self.root
        
        for char in title.lower:
            node = node.children.setdefault(char,TrieNode())
        node.is_end = True
        node.movie = movie 

    def _dfs(self,node,results):
        if node.is_end:
            results.append(node.movie)
        for char, next_node in node.children.item():
            self._dfs(next_node,results)
    def _traverse(self,string:str):
        node = self.root
        for char in string.lower():
            if char not in node.children:
                return None
        return node
    def search(self,title:str) -> bool:
        node = self._traverse(title)
        if node and node.is_end:
            return node.movie
        return None
    def prefix_search(self,prefix:str):
        node = self._traverse(prefix)
        if not node:
            return []
        results = []
        self._dfs(node,results)
        return results