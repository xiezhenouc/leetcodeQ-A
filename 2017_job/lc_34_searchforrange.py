'''
search a range
for example :
    1 2 3 4 4 4 4 4 6 7 
    0 1 2 3 4 5 6 7 8 8
    target value = 4
    return [3, 7]
    target value = 10
    return [-1, -1]
'''

class Solution(object):
    def searchRange(self, nums, target):
        rangeleft = -1
        rangeright = -1

        left = 0 
        right = len(nums) - 1
        mid = (left + right) / 2

        while left <= right:
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if nums[left] < target:
                    left += 1
                    right = mid
                if nums[left] == target:
                    rangeleft = left
                    break
            mid = (left + right) / 2
        print rangeleft

        left = 0 
        right = len(nums) - 1
        mid = (left + right) / 2

        while left <= right:
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if nums[right] > target:
                    left = mid
                    right -= 1
                if nums[right] == target:
                    rangeright = right
                    break
            mid = (left + right) / 2

        print rangeright

        return [rangeleft, rangeright]



if __name__ == '__main__':
    nums = [1, 3]
    target = 1 
    print Solution().searchRange(nums, target)
