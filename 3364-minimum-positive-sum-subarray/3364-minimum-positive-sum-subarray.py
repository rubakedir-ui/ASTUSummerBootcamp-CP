class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        min_sum = None
        for j in range(l, r + 1):
            for i in range(n - j + 1):
                sub = nums[i : i + j]
                current_sum = sum(sub)
                if current_sum > 0:
                    if min_sum is None:
                        min_sum = current_sum
                    else:
                        if current_sum < min_sum:
                            min_sum = current_sum
        if min_sum is not None:
            return min_sum
        else:
            return -1