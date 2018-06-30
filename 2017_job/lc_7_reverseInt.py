class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = 0 - x
       
        #sum
        Sum = 0
        while x > 0:
            digit = x % 10
            Sum = Sum * 10 + digit
            x = x / 10 
        
        #int(32) range
        if Sum >= 0xffffffff / 2:
            Sum = 0
        return sign * Sum

a = Solution()
print a.reverse(-123)
          
         
