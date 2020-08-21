class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0;
        temp=0;
        if len(nums)>0:
            ans=nums[0]
            temp=nums[0]
        for i in range(1,len(nums)):
            if temp>0:
                temp+=nums[i]
            else:
                temp=nums[i]         
            if temp>ans:
               ans=temp
        return ans