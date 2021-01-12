class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        pos = 0
        zeros = 0
        for i in nums:
            if i != 0:
                nums[pos]= i
                pos+=1
            else:
                zeros+=1
        for i in range(length-zeros,length):
            nums[i]=0
        pass
