class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = k
        right = k
        minimum = nums[k]
        answer = nums[k]

        while left > 0 or right < len(nums) - 1:
            if left == 0:
                right += 1
            elif right == len(nums) - 1:
                left -= 1
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
            else:
                right += 1
            minimum = min(minimum, nums[left], nums[right])
            length = right - left + 1
            score = minimum * length
            answer = max(answer, score)

        return answer 