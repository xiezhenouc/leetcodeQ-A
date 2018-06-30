class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #hash nums
        mydict = {}
        mylist = []
        length = len(nums)

        nums.sort()

        #print nums

        for i in range(length):
            mydict[nums[i]] = i
        
        i = 0
        #O(n^2)
        while i < length - 1:
            j = i + 1
            while j < length: 
                    #hash find
                    if 0-nums[i]-nums[j] in mydict:
                        k = int(mydict[0-nums[i]-nums[j]])
                        if k > j:
                            #print i, j, k 
                            
                            sublist = [nums[i], nums[j], nums[k]]
                            if sublist not in mylist:
                                mylist.append(sublist)
                                j += 1
                                #drop duplicates
                                while j < length and nums[j] == nums[j-1]:
                                    j += 1
                            else:
                                j += 1
                        else:
                            j += 1
                    else: 
                        j += 1 
            i += 1
        return mylist
nums = [-2,10,-14,11,5,-4,2,0,-10,-10,5,7,-11,10,-2,-5,2,12,-5,14,-11,-15,-5,12,0,13,8,7,10,6,-9,-15,1,14,11,-9,-13,-10,6,-8,-5,-11,6,-9,14,11,-7,-6,8,3,-7,5,-5,3,2,10,-6,-12,3,11,1,1,12,10,-8,0,8,-5,6,-8,-6,8,-12,-14,7,9,12,-15,-12,-2,-4,-4,-12,6,7,-3,-6,-14,-8,4,4,9,-10,-7,-4,-3,1,11,-1,-8,-12,9,7,-9,10,-1,-14,-1,-8,11,12,-5,-7]
#nums = [-1, 0, 1, 2, -1, -4]

a = Solution()
print a.threeSum(nums)
