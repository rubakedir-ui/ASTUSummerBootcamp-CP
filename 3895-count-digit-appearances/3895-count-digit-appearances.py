class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        count = 0
    
        for num in nums:
           for d in str(num):
              if d == str(digit):
                 count += 1
                
        return count