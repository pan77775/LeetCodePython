class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = ""
        left = ["{","[","("]
        right = ["}","]",")"]
        for i in s:
            if i in left:
                temp=temp+i
            elif temp != "" and right.index(i)==left.index(temp[-1]):
                    temp=temp[:-1]
            else:
                return False       
        if temp == "":
            return True
        else:
            return False