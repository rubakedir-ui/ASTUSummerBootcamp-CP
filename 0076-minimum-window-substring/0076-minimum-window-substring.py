class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)
        window = {}

        left = 0
        count = 0
        ans = ""

        for right in range(len(s)):
            c = s[right]

            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                count += 1

            while count == len(need):

                if ans == "" or right - left + 1 < len(ans):
                    ans = s[left:right+1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    count -= 1

                left += 1

        return ans