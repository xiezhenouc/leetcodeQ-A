class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        result = []
        
        while i < len(s):
            # odd number
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and left < right:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            if len(s[left+1:right]) > len(result):
                result = s[left+1:right]
            
            # even number
            left = i - 1
            right = i
            while left >= 0 and right < len(s) and left < right:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            if len(s[left+1:right]) > len(result):
                result = s[left+1:right]
 
            #loop
            i += 1
         
        return result

a = Solution()
str = ''

a.longestPalindrome(str)
 
