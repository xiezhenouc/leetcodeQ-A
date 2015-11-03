class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []

        alen = len(a) - 1
        blen = len(b) - 1
      
        i, j = alen, blen
        increment = 0
        while i >= 0 and j >= 0:
            curdigit = int(a[i]) + int(b[j]) + increment  
            if curdigit > 1:
                curdigit %= 2
                increment = 1
            else:
                increment = 0
            
            result.insert(0, str(curdigit))
            
            i -= 1
            j -= 1
        
        while i >= 0:
            curdigit = int(a[i]) + increment  
            if curdigit > 1:
                curdigit %= 2
                increment = 1
            else:
                increment = 0
            result.insert(0, str(curdigit))
            i -= 1

        while j >= 0:
            curdigit = int(b[j]) + increment  
            if curdigit > 1:
                curdigit %= 2
                increment = 1
            else:
                increment = 0
            result.insert(0, str(curdigit))
            j -= 1
        
        if increment > 0:
            result.insert(0, str(increment)) 

        return ''.join(result) 

if __name__ == '__main__':
    a = '1'
    b = '111'
    print Solution().addBinary(a, b)
                      
