class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
    
        for i in range(len(s) - 1):
           difference = abs(ord(s[i]) - ord(s[i+1]))
           score += difference
    
        return score