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