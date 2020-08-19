class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # x2str = str(x)
        # for i in range(len(x2str)/2):
        #     if x2str[i] != x2str[len(x2str)-i-1]:
        #         return False
        # return True
        if x<0 or x%10==0 and x!=0:
            return False;
        ans = 0;
        while (x>ans):
            ans = ans*10 + x%10
            x = x//10
        return (x==ans or x==ans//10);