"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

# Solution
# My solution:
def autocomplete(s, queries):
    result = []
    
    for query in queries:
        if query.startswith(s):
            result.append(query)
    
    return result

# More efficient solution: using Trie / Prefix Tree data structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def find_all_words(self, prefix):
        node = self.search_prefix(prefix)
        if not node:
            return []
        
        result = []
        self._dfs(node, prefix, result)
        return result
    
    def _dfs(self, node, current_prefix, result):
        if node.is_end_of_word:
            result.append(current_prefix)
        
        for char, child_node in node.children.items():
            self._dfs(child_node, current_prefix + char, result)

def preprocess(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

def autocomplete2(s, queries):
    trie = preprocess(queries)
    return trie.find_all_words(s)


# Tests
def test_autocomplete():
    test_cases = [
        {"prefix": "de", "words": ["dog", "deer", "deal"], "expected": ["deer", "deal"]},
        {"prefix": "cat", "words": ["dog", "deer", "deal", "apple"], "expected": []},
        {"prefix": "", "words": ["dog", "deer", "deal"], "expected": ["dog", "deer", "deal"]},
        {"prefix": "d", "words": ["dog", "deer", "deal", "cat", "apple"], "expected": ["dog", "deer", "deal"]},
        {"prefix": "De", "words": ["dog", "deer", "deal", "Dog", "Deer"], "expected": ["Deer"]},
        {"prefix": "deal", "words": ["dog", "deer", "deal", "dealer"], "expected": ["deal", "dealer"]},
        {"prefix": "dictionary", "words": ["dog", "deer", "deal", "dict"], "expected": []},
        {"prefix": "#t", "words": ["#tag", "#top", "hashtag"], "expected": ["#tag", "#top"]},
        {"prefix": "cafe", "words": ["cafe", "cafeteria", "coffee"], "expected": ["cafe", "cafeteria"]}
    ]
    
    for i, test in enumerate(test_cases):
        result = autocomplete2(test["prefix"], test["words"])
        assert result == test["expected"], f"Test {i+1} failed: got {result}, expected {test['expected']}"
        print(f"Test {i+1} passed!")

test_autocomplete()