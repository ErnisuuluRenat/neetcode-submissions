class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
    
        sh = {}
        th = {}

        for i in range(len(s)):
            char = s[i]
            if  char in sh:
                sh[char] += 1
            else:
                sh[char] = 1

        for i in range(len(t)):
            char = t[i]
            if  char in th:
                th[char] += 1
            else:
                th[char] = 1

        return sh == th