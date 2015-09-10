class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        mylist = list(str.lstrip())

        #+10 -10
        start = 0
        if len(mylist) > 0:
            if mylist[0] == '+':
                start = 1
            elif mylist[0] == '-':
                start = -1
            else:
                start = 0

        #check it is number  
        i = 0
        stop = 0
        if start != 0:
            i = 1
        while i < len(mylist):
            if not '0' <= mylist[i] <= '9':
                stop = i - 1
                break 
            else:
                stop = i
            i += 1

        #add sum
        numSum = 0
        i = 0
        if start != 0:
            i = 1
        while i < len(mylist) and i <= stop:
            numSum = numSum * 10 + int(mylist[i])
            i += 1

        #put signature
        if start != 0:
            numSum *= start
        
        if numSum > 2147483647:
            numSum = 2147483647
        if numSum < -2147483648:
            numSum = -2147483648       
        return numSum

a = Solution()
print a.myAtoi('+1') 

