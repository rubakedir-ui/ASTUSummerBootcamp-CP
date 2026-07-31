class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        for i in s:
            if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
                letters.append(i)

        ans = ""
        for i in s:
            if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
                ans = ans + letters.pop()
            else:
                ans = ans + i

        return ans 