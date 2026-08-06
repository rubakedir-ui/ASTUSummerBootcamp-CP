class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        i = 0
        ans = 0
        for h in houses:
            while ( i < len(heaters) - 1 and
                   abs(heaters[i+ 1] - h) <= abs(heaters[i] - h)):
                i += 1
            ans = max(ans, abs(heaters[i] - h))

        return ans