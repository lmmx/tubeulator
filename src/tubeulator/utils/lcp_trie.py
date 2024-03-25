"""LCP trie adapted from dict (char) trie at:
https://ychai.uk/notes/2019/03/03/Programming/Tricks-of-Python/
"""

from __future__ import annotations

__all__ = ["TrieNode", "Trie"]


class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie and aggregates it with existing nodes (longest
        common prefix nodes).
        """
        node = self.root
        # If no common ancestors, insert entire word
        if not node.data:
            node.data[word] = TrieNode()
            node.data[word].is_word = True
            return
        # Iterate through existing nodes
        while True:
            # Find the longest common prefix between the word and node keys
            lcp = ""
            lcp_key = None
            for key in node.data.keys():
                prefix = ""
                for i, (a, b) in enumerate(zip(word, key)):
                    if a == b:
                        prefix += a
                    else:
                        break
                if len(prefix) > len(lcp):
                    lcp = prefix
                    lcp_key = key
            if not lcp:
                # No common prefix, insert entire word as new node
                node.data[word] = TrieNode()
                node.data[word].is_word = True
                return
            # If entire common ancestor is found, insert below
            lcp_size = len(lcp)
            if lcp == lcp_key:
                node = node.data[lcp_key]
                word = word[lcp_size:]
            else:
                # Split the node at the branch point and insert the rest of the word below it
                new_node = TrieNode()
                node.data[lcp] = new_node
                new_node.data[lcp_key[lcp_size:]] = node.data.pop(lcp_key)
                if not word:
                    # The branch point is the word
                    new_node.is_word = True
                else:
                    # Put the remaining suffix below the LCP branch point node
                    partial_word = word[lcp_size:]
                    new_node.data[partial_word] = TrieNode()
                    new_node.data[partial_word].is_word = True
                return

    def search(self, word: str) -> None:
        """Returns if the word is in the trie."""
        node = self.root
        for letter in word:
            node = node.data.get(letter)
            if not node:
                return False
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        """Returns if there is any word in the trie
        that starts with the given prefix.
        """
        node = self.root
        for letter in prefix:
            node = node.data.get(letter)
            if not node:
                return False
        return True

    def get_start(self, prefix: str) -> list[str]:
        """Returns words started with prefix"""

        def _get_key(pre, pre_node):
            words_list = []
            if pre_node.is_word:
                words_list.append(pre)
            for x in pre_node.data.keys():
                words_list.extend(_get_key(pre + str(x), pre_node.data.get(x)))
            return words_list

        words = []
        if not self.starts_with(prefix):
            return words
        if self.search(prefix):
            words.append(prefix)
            return words
        node = self.root
        for letter in prefix:
            node = node.data.get(letter)
        return _get_key(prefix, node)

    def print_data(self) -> None:
        def dfs(node, level):
            if not node:
                return
            for key, child in node.data.items():
                print("  " * level + key)
                dfs(child, level + 1)

        dfs(self.root, 0)

    def walk(self):
        def dfs(node):
            if not node:
                return {}
            children = {}
            for letter, child in node.data.items():
                children[letter] = dfs(child)
            return {
                letter: subtree if any(subtree.values()) else list(subtree)
                for letter, subtree in children.items()
            }

        return dfs(self.root)

    @classmethod
    def from_strings(cls, strings: list[str]) -> Trie:
        trie = cls()
        for s in strings:
            trie.insert(s)
        return trie
