class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num % 9 == 0:
            return 9
        return num % 9

if __name__ == '__main__':
    print Solution().addDigits(9)
        
