class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return not n % 4 == 0

if __name__ == '__main__':
    for i in range(20):
        print Solution().canWinNim(i)
