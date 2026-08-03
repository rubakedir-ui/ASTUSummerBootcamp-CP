class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        count = 0
        for i in range(n):
            left = colors[(i - 1) % n]
            middle = colors[i]
            right = colors[(i + 1) % n]

            if middle != left and middle != right:
                count += 1
                
        return count 