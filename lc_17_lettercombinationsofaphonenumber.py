'''
Letter Combinations of a Phone Number
'''

class Solution(object):
    def letterCombinations(self, digits):
        mydict = { 
               '2':'abc',
               '3':'def',
               '4':'ghi',
               '5':'jkl',
               '6':'mno',
               '7':'pqrs',
               '8':'tuv',
               '9':'wxyz'
             }

        result = []

        digitslen = len(digits)
        if digitslen == 0:
            return []
        
        if digitslen == 1:
            k = 0
            while k < len(mydict[digits[0]]):
                result.append(mydict[digits[0]][k])
                k += 1
            return result

        #digitslen > 0
        prefixresult = self.letterCombinations(digits[0:digitslen-1])

        i = 0
        while i < len(prefixresult):
            j = 0
            while j < len(mydict[digits[digitslen-1]]):
                result.append(prefixresult[i] + mydict[digits[digitslen-1]][j])
                j += 1
            i += 1

        return result
if __name__ == '__main__':
    digits = ''
    print Solution().letterCombinations(digits)
