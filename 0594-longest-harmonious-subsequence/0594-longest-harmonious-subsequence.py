class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        ans = 0

        for num in count:

            if num + 1 in count:

                length = count[num] + count[num + 1]

                ans = max(ans, length)


        return ans
