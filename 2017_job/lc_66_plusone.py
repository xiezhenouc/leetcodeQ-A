class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """   
        for i in range(len(digits)):
            digits[i] = str(digits[i]) 
        mystr = ''.join(digits)
        result = list(str(int(mystr) + 1))
        for i in range(len(result)):
            result[i] = int(result[i])
        return result

if __name__ == '__main__':
    digits = [9, 9]
    print Solution().plusOne(digits)
