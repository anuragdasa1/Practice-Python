class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False

        reverse = str(x)[::-1] 
        if int(reverse) == x:
            return True
        else: return False
        """
        :type x: int
        :rtype: bool
        """
        