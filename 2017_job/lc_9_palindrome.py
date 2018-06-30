class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xcopy = x

        if x < 0:
            return False
       
        #sum
        Sum = 0
        while x > 0:
            digit = x % 10
            Sum = Sum * 10 + digit
            x = x / 10 
        
        if Sum >= 0xffffffff / 2:
            Sum = 0
        
        return Sum == xcopy

a = Solution()
print a.isPalindrome(121564)
