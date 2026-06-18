class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def get_score(student):
             return student[k]

        score.sort(key=get_score, reverse=True)

        return score