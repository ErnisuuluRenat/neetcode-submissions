class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
    
        sh = {}
        th = {}

        for char in s:
            if  char in sh:
                sh[char] += 1
            else:
                sh[char] = 1

        for char in t:
            if  char in th:
                th[char] += 1
            else:
                th[char] = 1

        return sh == th