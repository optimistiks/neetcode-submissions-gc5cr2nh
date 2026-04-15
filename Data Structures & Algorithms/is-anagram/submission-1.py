class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1
        for letter in t:
            letters[letter] = letters.get(letter, 0) - 1
        return all(freq == 0 for freq in letters.values())

