class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        if string[0] == "-":
            string_rev = "-" + string[:0:-1]
        else:
            string_rev = string[::-1]
        ans = int(string_rev)
        if ans > 2**31 or ans < -(2**31):
            return 0
        else:
            return ans