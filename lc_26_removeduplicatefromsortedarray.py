'''
remove duplicates from sorted array
'''
class Solution(object):
    def removeDuplicates(self, nums):
        p = 0
        q = 0
        numslen = len(nums)
        if numslen == 0:
            return 0

        while q < numslen:
            if nums[p] == nums[q]:
                q += 1
            else:
                p += 1
                nums[p] = nums[q]
                q += 1
        print nums

        return p + 1

if __name__ == '__main__':
    nums = []
    print Solution().removeDuplicates(nums)
