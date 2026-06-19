class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 1
        streak = 1

        for i in range(1, len(prices)):

            if prices[i-1] - prices[i] == 1:
                streak += 1
            else:
                streak = 1

            ans += streak

        return ans