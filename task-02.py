from trie import Trie, TrieNode

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings: list[str]) -> str:
        if not strings:
            raise TypeError(
                f"Illegal argument for findLongestCommonWord: strings must be a non-empty list of strings"
            )
        if len(strings) == 1:
            return strings[0]

        prefix = None
        self.put(strings[0])
        for i, word in enumerate(strings[1:]):
            word_prefix = self._put_with_prefix(word, i)
            if not prefix or len(word_prefix) < len(prefix):
                prefix = word_prefix
        
        return prefix

    def _put_with_prefix(self, word: str, value: int) -> str:
        if not isinstance(word, str) or not word:
            raise TypeError(
                f"Illegal argument for put: word = {word} must be a non-empty string"
            )

        current = self.root
        prefix = ""
        add_prefix = True
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
                add_prefix = False
            elif not current.children[char].value is None:
                add_prefix = False
            current = current.children[char]
            if add_prefix:
                prefix += char
        if current.value is None:
            self.size += 1
        current.value = value     
        return prefix   

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed!")