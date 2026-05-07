class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        sH = dict(enumerate(s))
        tH = dict(enumerate(t))

        return sorted(sH.values()) == sorted(tH.values())