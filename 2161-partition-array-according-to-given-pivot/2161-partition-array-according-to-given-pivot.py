class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        small = []
        equal = []
        large = []

        for num in nums:

            if num < pivot:
                small.append(num)

            elif num == pivot:
                equal.append(num)

            else:
                large.append(num)

        return small + equal + large