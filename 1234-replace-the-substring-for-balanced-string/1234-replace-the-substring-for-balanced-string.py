class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        target = n // 4

        count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}

        for i in s:
            count[i] += 1

        if count['Q'] == target and count['W'] == target and count['E'] == target and count['R'] ==target:
            return 0

        left = 0
        ans = n

        for right in range(n):
            count[s[right]] -= 1

            while (count['Q'] <= target and count['W'] <= target and
                   count['E'] <= target and count['R'] <= target):

                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1

        return ans