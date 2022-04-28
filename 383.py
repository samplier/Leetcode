from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransom_hash = Counter(ransomNote)
        magazine_hash = Counter(magazine)

        for key in ransom_hash.keys():
            if key not in magazine_hash or magazine_hash[key] < ransom_hash[
                key]:
                return False
        return True
# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
