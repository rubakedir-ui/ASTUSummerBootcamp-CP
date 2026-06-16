class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            center = (left + right) // 2

            if nums[center] == target:
                return center

            elif nums[center] < target:
                left = center + 1

            else:
                right = center - 1

        return left