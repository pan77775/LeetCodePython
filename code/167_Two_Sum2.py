class Solution(object):
    def twoSum(self, numbers, target):
        for j in range(1,len(numbers)):
            if numbers[0]+numbers[j]==target:
                return[0+1,j+1]
        temp = numbers[0]
        for i in range(1,len(numbers)):
            if numbers[i]>temp:
                temp = numbers[i]
                for j in range(i+1,len(numbers)):
                    if numbers[i]+numbers[j]==target:
                        return[i+1,j+1]
        return [0,1]
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        