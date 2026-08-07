class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        count_0 = 0
        count_1 = 0
        total_substrings = 0

        for right in range(len(s)):
            if s[right] == "0":
                count_0 += 1
            else:
                count_1 += 1

            while count_0 > k and count_1 > k:
                if s[left] == "0":
                    count_0 -= 1
                else:
                    count_1 -= 1
                left += 1
            total_substrings += right - left + 1

        return total_substrings