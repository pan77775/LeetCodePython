class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        for i in nums:
            temp = temp^i
        return temp